import sys
import nbformat
from PIL import Image, ImageDraw
from nbformat.v4 import new_notebook, new_markdown_cell

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
    notebook_path = f'notebooks/{notebook_name}'
    try:
        add_deprecation_notice(notebook_path)
        print(f"Deprecation notice added to {notebook_name}.")
    except FileNotFoundError:
        print(f"Notebook {notebook_name} not found in notebooks/ folder.")
        sys.exit(1)
