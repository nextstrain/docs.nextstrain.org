# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Fetch docs --------------------------------------------------------------

import subprocess
subprocess.check_call([sys.executable or "python", './fetch-docs.py'])

# -- Project information -----------------------------------------------------

project = 'Nextstrain'
copyright = '2021, Trevor Bedford and Richard Neher'
author = 'The Nextstrain Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
    'sphinxarg.ext',
    'sphinx.ext.autodoc',
    'sphinx_tabs.tabs',
    'sphinx.ext.graphviz',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nextstrain-sphinx-theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

html_theme_options = {
    'display_version': False,
    'logo_only': True,
    'collapse_navigation': False,
    'titles_only': True,
}

graphviz_output_format = "svg"


# -- Cross-project references ------------------------------------------------

intersphinx_mapping = {
    'augur': ('https://docs.nextstrain.org/projects/augur/en/stable', None),
    'auspice': ('https://docs.nextstrain.org/projects/auspice/en/stable', None),
    'cli': ('https://docs.nextstrain.org/projects/cli/en/stable/', None),
    'nextclade': ('https://docs.nextstrain.org/projects/nextclade/en/stable/', None),
    'ncov': ('https://docs.nextstrain.org/projects/ncov/en/latest/', None)
}
