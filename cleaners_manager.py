import logging
import os
from pathlib import Path
import shutil
import subprocess
from typing import Dict, List, Optional, Set


class MrCleanersManager:
    def __init__(
        self,
        test_dir: Optional[str] = None,
        dry_run: bool = True,
        backup: bool = False,
        restore: bool = False,
        auto_dir_name: str = "Tests"
    ):
        self.setup_logging()
        self.test_dir = Path(test_dir) if test_dir else None
        self.dry_run = dry_run
        self.backup = backup
        self.restore = restore
        self.auto_dir_name = auto_dir_name
        self.backup_dir = Path("backup_cleanup")
        self.files_with_issues: Set[Path] = set()

    @staticmethod
    def setup_logging():

        """
        Configures logging for the cleanup process if not already configured.
        Outputs logs to both a file (cleanup.log) and the console.
        """

        if not logging.getLogger().hasHandlers():
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s [%(levelname)s] %(message)s",
                handlers=[
                    logging.FileHandler("cleanup.log", mode='w'),
                    logging.StreamHandler()
                ]
            )

    # MrCleanersManager.run_cleanup
    @staticmethod
    def run_cleanup(
        test_dir: Optional[str] = None,
        dry_run: bool = True,
        backup: bool = False,
        restore: bool = False,
        auto_dir_name: str = "Tests"
    ):

        """
        Analyzes test files to detect unused imports, optionally backs up affected files,
        automatically fixes issues by removing unused imports, or restores files from backup.

        Args:
            test_dir (Optional[str]): Path to the test directory. If not specified, auto-detection is used.
            dry_run (bool): If True, only reports issues without making changes. Defaults to True.
            backup (bool): If True and dry_run is False, creates a backup of affected files before fixing.
            restore (bool): If True, restores test files from the backup directory and skips analysis/fixing.
            auto_dir_name (str): Directory name to search for test files if test_dir is not specified.

        Notes:
            - If `restore=True`, backup restoration is prioritized over any analysis or fixing.
            - If `dry_run=True`, no files will be modified.
            - Only files with detected issues are backed up.
        """

        manager = MrCleanersManager(
            test_dir=test_dir,
            dry_run=dry_run,
            backup=backup,
            restore=restore,
            auto_dir_name=auto_dir_name
        )
        manager.run()

    def run(self):

        """
        Main execution sequence:
        - Finds the test directory.
        - Runs dry-run analysis to detect unused imports.
        - Optionally creates backups of affected files.
        - Optionally fixes unused imports.
        - Optionally restores files from backup if requested.

        All steps are logged to cleanup.log.
        """

        logging.info("=== Start of MrCleanersManager process ===")
        logging.info(f"Current working directory: {os.getcwd()}")

        if self.test_dir:
            test_path = self.test_dir
            if not test_path.is_absolute():
                test_path = Path.cwd() / test_path
            logging.info(f"Path to directory provided manually: {test_path}")
        else:
            logging.info(f"Path not specified. Searching for directory '{self.auto_dir_name}/' automatically...")
            test_path = self.find_tests_dir()
            if not test_path:
                logging.error(f"Directory '{self.auto_dir_name}/' not found. Please run the script from the project root where '{self.auto_dir_name}/' is located.")
                return

        if not test_path.exists() or not test_path.is_dir():
            logging.error(f"Specified directory '{test_path}' does not exist or is not a directory.")
            return

        if self.restore:
            self.restore_backup(test_path)
            logging.info("=== Backup restoration process completed ===")
            return

        # Step 1: Always run dry-run first to collect issues
        self.run_ruff(test_path, dry_run_mode=True)

        # Step 2: Create backup if required
        if self.backup and not self.dry_run:
            logging.info("Starting backup of files with issues...")
            self.create_backup()
            logging.info("Backup completed.")

        # Step 3: If dry_run=False, then run ruff --fix after backup
        if not self.dry_run:
            self.run_ruff(test_path, dry_run_mode=False)

        logging.info("=== End of MrCleanersManager process ===")

    def find_tests_dir(self) -> Optional[Path]:

        """
        Searches recursively for the test directory starting from the current working directory.

        Returns:
            Path to the test directory if found, otherwise None.
        """

        current_dir = Path.cwd()
        for path in current_dir.rglob(self.auto_dir_name):
            if path.is_dir():
                return path
        return None

    def create_backup(self):

        """
        Creates a backup of all Python files that have detected unused imports.
        Backs up into the 'backup_cleanup/' directory, preserving the folder structure.
        Only files with issues are copied.
        """

        if not self.backup_dir.exists():
            self.backup_dir.mkdir(parents=True)

        if not self.files_with_issues:
            logging.warning("No files with issues detected. Nothing to backup.")
            return

        logging.info(f"Backing up files to: {self.backup_dir}")
        for relative_file_path in self.files_with_issues:
            source_file = Path.cwd() / relative_file_path
            backup_path = self.backup_dir / relative_file_path
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            if source_file.exists():
                shutil.copy2(source_file, backup_path)
                logging.info(f"✅ Copied: {source_file} → {backup_path}")
            else:
                logging.warning(f"⚠️ File not found during backup: {source_file}")

    def restore_backup(self, test_path: Path):

        """
        Restores previously backed-up Python files from the 'backup_cleanup/' directory
        back into the specified test directory.

        Args:
            test_path (Path): Path to the test directory where files should be restored.
        """

        if not self.backup_dir.exists():
            logging.error("Backup folder backup_cleanup/ not found. Cannot perform restoration.")
            return

        logging.info("Starting restoration of files from backup...")
        for backup_file in self.backup_dir.rglob("*.py"):
            target_path = test_path / backup_file.relative_to(self.backup_dir)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(backup_file, target_path)
            logging.info(f"♻️ Restored: {backup_file} → {target_path}")

    def run_ruff(self, test_path: Path, dry_run_mode: bool):

        """
        Executes the ruff tool to analyze or fix unused imports in the test files.

        Args:
            test_path (Path): Path to the directory to analyze.
            dry_run_mode (bool): If True, only reports issues without fixing; if False, applies fixes.
        """

        cmd = ["ruff", "check", str(test_path), "--select", "F401"]
        if not dry_run_mode:
            cmd.append("--fix")

        mode = "Dry-run" if dry_run_mode else "Fix"
        logging.info(f"Running {mode} command: {' '.join(cmd)}")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            logging.info(f"ruff finished without errors. No unused imports found. ({mode})")
        else:
            if dry_run_mode:
                logging.info("Dry-run mode: Displaying files with unused imports (no changes made).")
                grouped_errors: Dict[str, List[str]] = {}
                for line in result.stdout.strip().splitlines():
                    if ".py:" in line and "F401" in line:
                        parts = line.split(":")
                        if len(parts) >= 4:
                            full_file_path = Path(parts[0])
                            try:
                                relative_path = full_file_path.relative_to(Path.cwd())
                                self.files_with_issues.add(relative_path)
                                line_info = f"Line {parts[1]}:{parts[2]} — {line.split('`')[-2]}"
                                grouped_errors.setdefault(relative_path, []).append(line_info)
                            except ValueError:
                                line_info = f"Line {parts[1]}:{parts[2]} — {line.split('`')[-2]}"
                                grouped_errors.setdefault(full_file_path, []).append(line_info)
                                self.files_with_issues.add(full_file_path)
                for file, errors in grouped_errors.items():
                    logging.info(f"[DRY-RUN] {file}:")
                    for err in errors:
                        logging.info(f"    {err}")
            else:
                logging.info("Unused imports successfully removed.")

        logging.info(f"Full ruff output:\n{result.stdout}")
        if result.stderr:
            logging.warning(f"ruff stderr:\n{result.stderr}")


    # Example usage:
    # MrCleanersManager.run_cleanup(test_dir="Tests/", dry_run=False, backup=True)
    # MrCleanersManager.run_cleanup(test_dir="Tests/", restore=True)
    # ATTENTION! The method must be executed in a file located in the root of the project,
    # so that the tests folder is a subfolder in this project.
