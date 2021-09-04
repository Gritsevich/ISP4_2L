#!/usr/bin/env python

from platform import python_version_tuple

import setuptools


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if python_version_tuple()[0] < "3":
    raise ValueError("Error python version. Need python3 and more")

setup(
    name="dump",
    version="1.0.0",
    description="Dump function to YAML/JSON/TOML",
    author="Rina",
    url="https://github.com/Gritsevich/ISP_2L",
    license="MIT",
    setup_requires=["wheel"],
    install_requires=["pyyaml", "toml", "wheel"],
    packages=["tools", "parsers", "parsers/json", "parsers/yaml", "parsers/toml", "factory", "application"],
    entry_points={"console_scripts": "dump=application.command_line:main"},
)
