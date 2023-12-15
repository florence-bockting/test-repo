# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
#import sys

#sys.path.insert(0, os.path.abspath("../../example_project"))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2023, flo'
author = 'flo'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Support automatic documentation
    "sphinx.ext.coverage",  # Automatically check if functions are documented
    "sphinx.ext.mathjax",  # Allow support for algebra
    "sphinx.ext.viewcode",  # Include the source code in documentation
    "sphinx.ext.githubpages",  # Build for GitHub pages
    "numpydoc",  # Support NumPy style docstrings
]   "myst_nb",

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']


# do not execute jupyter notebooks when building docs
nb_execution_mode = "off"

# download notebooks as .ipynb and not as .ipynb.txt
html_sourcelink_suffix = ""

suppress_warnings = [
    f"autosectionlabel._examples/{filename.split('.')[0]}"
    for filename in os.listdir("notebooks/")
    if os.path.isfile(os.path.join("notebooks/", filename))
]  # Avoid duplicate label warnings for Jupyter notebooks.

remove_from_toctrees = ["_autosummary/*"]