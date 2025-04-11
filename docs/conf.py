import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Multi-Repo Documentation'
author = 'Dan'
release = '0.1'

extensions = ['sphinx_needs']

# Automatically include needs from other repos' GitHub Pages
needs_external_needs = [
    {
        'url': 'https://dcalavrezo-qorix.github.io/repoA/needs.json',
        'base_url': 'https://dcalavrezo-qorix.github.io/repoA/',
        'id_prefix': 'MODA_'
    },
    {
        'url': 'https://dcalavrezo-qorix.github.io/repoB/needs.json',
        'base_url': 'https://dcalavrezo-qorix.github.io/repoB/',
        'id_prefix': 'MODB_'
    }
]

# Optional, if you have internal needs in this repo too
# needs_id_prefix = "AGG_"
# needs_id_required = True

master_doc = 'index'
html_theme = 'alabaster'  
