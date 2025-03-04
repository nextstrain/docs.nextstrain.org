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

from datetime import datetime
project = 'Nextstrain'
copyright = f'{datetime.now().year}, Trevor Bedford and Richard Neher'
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
    'nextstrain.sphinx.theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    'snippets',
]

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
    'version_selector': False,
    'subproject': False, # For new theme versions
    'logo_only': True,   # For old theme versions
    'collapse_navigation': False,
    'titles_only': True,
}

graphviz_output_format = "svg"


# -- Cross-project references ------------------------------------------------

intersphinx_mapping = {
    'augur': ('https://docs.nextstrain.org/projects/augur/page/', None),
    'auspice': ('https://docs.nextstrain.org/projects/auspice/page/', None),
    'cli': ('https://docs.nextstrain.org/projects/cli/page/', None),
    'nextclade': ('https://docs.nextstrain.org/projects/nextclade/page/', None),
    'ncov': ('https://docs.nextstrain.org/projects/ncov/page/', None),
    'python': ('https://docs.python.org/3/', None),
}


# -- Linkchecking ------------------------------------------------------------

## NOTE: for both sets of regular expressions that follow, the
## underlying linkchecker code uses `re.match()` to apply them to URLs
## — so there's already an implicit "only at the beginning of a
## string" matching happening, and something like a plain `r'google'`
## regular expression will _NOT_ match all google.com URLs.
linkcheck_ignore = [
     # we have links to localhost for explanatory purposes; obviously
     # they will never work in the linkchecker
     r'^http://127\.0\.0\.1:\d+',
     r'^http://localhost:\d+',
     # these URLs block the client the linkchecker uses
     r'^https://www\.pnas\.org/doi/10\.1073/pnas\.1507071112',
     r'^https://www\.ncbi\.nlm\.nih\.gov/books/NBK25501',
     # These URLs fail in GH Actions, but succeeds locally.
     r'^https://wiki\.mozilla\.org/CA/Included_Certificates',
     r'^https://www\.gnu\.org/software/bash/manual/bash\.html\#What-is-Bash_003f',
     # we specifically use this as an example of a link that _won't_ work
     r'^https://nextstrain\.org/ncov/gisaid/21L/global/6m/2024-01-10',
]
linkcheck_anchors_ignore_for_url = [
     # colorbrewer uses pseudo-anchors, ala Github. Converting the `#`
     # to `?` loads the same page, but it also appends the query
     # string as a pseudo-anchor, so the URL ends up looking very ugly
     # and potentially misleading. Let's just ignore the anchor...
     r'^https://colorbrewer2\.org',
     # Github uses anchor-looking links for highlighting lines but
     # handles the actual resolution with Javascript, so skip anchor
     # checks for Github URLs:
     r'^https://github\.com',
]
