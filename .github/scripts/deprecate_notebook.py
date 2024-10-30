import sys
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

def find_notebook(notebook_name):
    # Start from the repository root (current working directory in the GitHub runner)
    repo_root = os.getcwd()
    
    # Walk through all subdirectories in the repository to find the notebook file
    print(f"Searching for {notebook_name} in the repository root and its subdirectories...")
    for dirpath, _, filenames in os.walk(repo_root):
        print(f"Checking directory: {dirpath}")  # Debugging output
        if notebook_name in filenames:
            notebook_path = os.path.join(dirpath, notebook_name)
            print(f"Found notebook at: {notebook_path}")
            return notebook_path
    print(f"Notebook {notebook_name} not found in the repository or its subfolders.")
    return None

def add_deprecation_notice(notebook_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add the "deprecated" tag in notebook metadata
    nb.metadata['deprecated'] = 'true'
    
    # Create a Markdown cell with the deprecation warning
    deprecation_warning = (
        "**⚠️ Deprecation Notice**\n\n"
        "**This notebook will soon be deprecated.**\n\n"
        "Please consider using an updated version or alternative resources.\n\n"
        "*This warning is automatically generated.*"
    )
    deprecation_notice_cell = new_markdown_cell(deprecation_warning)
    
    # Insert the deprecation notice at the top of the notebook
    nb.cells.insert(0, deprecation_notice_cell)
    
    # Save the modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    notebook_name = sys.argv[1]
    notebook_path = find_notebook(notebook_name)

    if notebook_path:
        add_deprecation_notice(notebook_path)
        print(f"Deprecation notice added to {notebook_path}.")
    else:
        print(f"Notebook {notebook_name} not found in the repository or its subfolders.")
        sys.exit(1)
