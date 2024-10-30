import sys
import os
import nbformat
from PIL import Image, ImageDraw
from nbformat.v4 import new_notebook, new_markdown_cell

def find_notebook(notebook_name, root_folder='notebooks'):
    # Set the target folder to the notebooks directory at the repository root
    target_folder = os.path.join(os.getcwd(), root_folder)
    
    # Walk through all subdirectories to find the notebook file
    print(f"Searching for {notebook_name} in {target_folder} and its subdirectories...")
    for dirpath, _, filenames in os.walk(target_folder):
        print(f"Checking directory: {dirpath}")  # Debugging output
        if notebook_name in filenames:
            notebook_path = os.path.join(dirpath, notebook_name)
            print(f"Found notebook at: {notebook_path}")
            return notebook_path
    print(f"{notebook_name} not found in {target_folder} or its subdirectories.")
    return None

def add_deprecation_notice(notebook_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add the "deprecated" tag in notebook metadata
    nb.metadata['deprecated'] = 'true'
    
    # Create a deprecation notice image
    img = Image.new('RGB', (800, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (799, 99)], outline="red", width=5)
    draw.text((10, 35), "This notebook will soon be deprecated.", fill="red")
    img_path = 'deprecated_notice.png'
    img.save(img_path)
    
    # Add the image to the first cell as Markdown with a red border
    deprecation_notice_cell = new_markdown_cell(f"![Deprecation Notice](attachment:{img_path})")
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
        print(f"Notebook {notebook_name} not found in notebooks/ or i
