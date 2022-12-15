"""Package setup."""

from setuptools import setup

setup(
    name="ntia-conformance-checker",
    version="0.0.1",
    packages=["ntia_conformance_checker", "ntia_conformance_checker.cli_tools"],
    install_requires=[
        "spdx-tools @ git+https://github.com/linynjosh/tools-python#egg=spdx-tools",
    ],
)
