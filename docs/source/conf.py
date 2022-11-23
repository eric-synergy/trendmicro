# Configuration file for the Sphinx documentation builder.

# -- Project information

from datetime import date
# -- Project information -----------------------------------------------------

project = 'Veeam'
copyright = str(date.today().year) + ', Eric W'
author = 'Eric W'

# The full version, including alpha/beta/rc tags
release = '1.0'



# -- General configuration

extensions = [
]

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_title = "TM"
html_theme_options = {}