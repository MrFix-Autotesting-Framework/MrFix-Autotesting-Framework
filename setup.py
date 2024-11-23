from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "The Mr Fix module is designed to create autotests written in Python for testing UI, API, PostgreSQL, Security, and Performance Testing."

setup(
    name="mrfix",
    version="7.0.3",
    author="Valerii Zhuravlev",
    author_email="valerii.zhuravlev.for.job@gmail.com",
    description="The Mr Fix module is designed to create autotests written in Python for testing UI, API, PostgreSQL, Security, and Performance Testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "selenium",
        "pyperclip",
        "beautifulsoup4",
        "cryptography",
        "psycopg2-binary",
        "requests",
        "httpx",
        "pytest",
        "loguru",
        "sh"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

