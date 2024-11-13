from setuptools import setup

setup(
    name="mrfix",
    version="7.0.1",
    description="The Mr Fix module is designed to create autotests written in Python for testing UI, API, PostgreSQL, Security and Perfomance Testing.",
    packages=["mrfix"],
    install_requires=[
        "selenium",
        "pyperclip",
        "beautifulsoup4",
        "cryptography",
        "psycopg2-binary",
        "cryptography",
        "requests",
        "httpx",
        "pytest",
        "loguru",
        "sh"
    ],
)
