# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'Schema-Miner'
copyright = '2025, Sameer Sadruddin'
author = 'Sameer Sadruddin'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    "sphinx.ext.autodoc"
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    "logo_only": True,
    'version_selector': True,
    'language_selector': True,
    'collapse_navigation': False,
    'sticky_navigation': False,
    'includehidden': True,
    'titles_only': False
}

html_css_files = [
    'css/custom.css',
]

html_show_sourcelink = True
html_context = {
    "display_github": True,
    "github_user": "sciknoworg",
    "github_repo": "schema-miner",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

html_logo = "img/schema-miner-logo2.png"
autoclass_content = "both"