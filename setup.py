#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
    "pytest-flake8",
]

setup(
    author="Victor Ng",
    author_email="vng@mozilla.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A collection of util functions for extracting domains from urls.",
    include_package_data=True,
    install_requires=requirements,
    keywords="domain_utils",
    license="MPL 2.0",
    long_description=readme + "\n\n" + history,
    name="domain_utils",
    packages=find_packages(exclude=["tests", "tests/*"]),
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/mozilla/private-distributed-learning",
    version="0.1.0",
    zip_safe=False,
)
