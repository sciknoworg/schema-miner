# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import tomllib

sys.path.insert(0, os.path.abspath("../../"))

project = "Schema-Miner Pro"
copyright = "2025, Sameer Sadruddin"
author = "Sameer Sadruddin"
with open(os.path.abspath("../../pyproject.toml"), "rb") as pyproject:
    release = tomllib.load(pyproject)["project"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_theme_options = {
    "sidebar_hide_name": True,
    "source_repository": "https://github.com/sciknoworg/schema-miner/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "light_css_variables": {
        "color-brand-primary": "#007c92",
        "color-brand-content": "#005f73",
    },
    "dark_css_variables": {
        "color-brand-primary": "#50d2df",
        "color-brand-content": "#7de3ec",
    },
}

html_css_files = [
    "css/custom.css",
]

html_show_sourcelink = True
html_context = {
    "display_github": True,
    "github_user": "sciknoworg",
    "github_repo": "schema-miner",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

html_logo = "img/schema-miner-pro-logo-transparent.png"
autoclass_content = "both"
