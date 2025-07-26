# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""
Sphinx documentation builder configuration file.

For a full list of available options, see:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from __future__ import annotations

import os
import sys
from typing import List

# Path setup
sys.path.insert(0, os.path.abspath(".."))

# Add any paths that contain templates here, relative to this directory.
templates_path: List[str] = ["_templates"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Project information
project = "NTIA Conformance Checker"  # pylint: disable=C0103
project_copyright = "2022-%Y SPDX contributors"  # pylint: disable=C0103
author = "SPDX contributors"  # pylint: disable=C0103

# The theme to use for HTML and HTML Help pages.
html_theme = "sphinx_rtd_theme"  # pylint: disable=C0103

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []
