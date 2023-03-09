import os
import sys

sys.path.insert(0, os.path.abspath("../wheat-yield-prediction-toolkit"))

# -- Project information -----------------------------------------------------
project = "wheat-yield-prediction-toolkit"
author = "mr. noureddine ech-chouky"

# -- General configuration ---------------------------------------------------
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.napoleon"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for autodoc ----------------------------------------------------
# Use the following to set the path to your package.
# For example, if your modules are in the wheat_yield_prediction_toolkit/core directory:
# autodoc_mock_imports = ['numpy']
# autodoc_mock_imports = ['pandas']
# autodoc_mock_imports = ['sklearn']
# autodoc_mock_imports = ['seaborn']

# For example, if your modules are in the wheat_yield_prediction_toolkit directory:
# autodoc_mock_imports = ['core']

# Replace "core" with the name of the directory containing your modules.
autodoc_mock_imports = ["core"]

# This value is a list of glob-style patterns that should be excluded when
# looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# This value contains a list of modules to be mocked up. This is useful when
# some external dependencies are not met at build time and break the building
# process.
# Example: autodoc_mock_imports = ['numpy', 'pandas']
# autodoc_mock_imports = ['numpy', 'pandas']
