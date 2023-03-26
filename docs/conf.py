# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NanoSSO'
copyright = '2023, Nat'
author = 'Nat'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autoapi.extension']

# autoapi config
autoapi_dirs = ['../NanoSSO']
autoapi_add_toctree_entry = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']

html_title = "NanoSSO Docs"
html_context = {
    "default_mode": "dark",
    "github_user": "NullsecSpace",
    "github_repo": "NanoSSO",
    "github_version": "main",
    "doc_path": "docs",
}
html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_depth": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/NullsecSpace/NanoSSO",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/NanoSSO",
            "icon": "fa-solid fa-box",
            "type": "fontawesome",
        },
        {
            "name": "NullsecSpace",
            "url": "https://nullsec.space",
            "icon": "fa-solid fa-star",
            "type": "fontawesome",
        }
    ]
}
