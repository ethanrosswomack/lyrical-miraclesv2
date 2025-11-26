---
title: Config Script
source_file: Hawk_Eye_Dev_Notebooks copy/Hawk_Eye_Store/Config_Script.ipynb
---

```python
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

# Define the base directory where the store structure will be created
base_dir = os.path.expanduser("~/Notebooks/Omniversal-Server/Hawk_Eye_Dev_Notebooks/Hawk_Eye_Store")

# Ensure base directory exists
os.makedirs(base_dir, exist_ok=True)

# Debugging information
print(f"📂 Base directory set to: {base_dir}")
print(f"Current working directory: {os.getcwd()}")
print(f"Does base directory exist? {'✅ Yes' if os.path.exists(base_dir) else '❌ No'}")

# Define the merchandise structure
merch_structure = {
    "Album-Inspired Collections": {
        "Full Disclosure Collection": ["Truth Seeker Graphic Tee", "Disclosure Hoodie"],
        "Behold A Pale Horse Collection": ["Pale Rider Snapback", "Prophecy Long Sleeve Tee"],
        "Milabs Merchandise": ["Abductee Glow-in-the-Dark Tee", "Mind Control Beanie"],
        "Shadow Banned Apparel": ["Glitch in the System Tee", "Unsilenced Face Mask"]
    },
    "Limited Edition Drops": {
        "Vigilant Eyes Tour Collection": [],
        "Rhyme and Reason Collaboration Series": [],
        "Lyrical Legacy Vintage Collection": [],
        "Conscious Threads Eco-Friendly Line": []
    },
    "Best Sellers": ["Sharp Vision Graphic Tee", "Lyrical Precision Hoodie", "Hawk Eye View Snapback"],
    "Custom Merch Creator": ["Choose Base Item", "Add Lyrics/Album Art", "Customize Design"]
}

# Function to create a notebook
def create_notebook(filepath, content):
    nb = new_notebook()
    nb.cells.append(new_markdown_cell(content))
    
    with open(filepath, 'w') as f:
        nbformat.write(nb, f)

# Loop through merchandise categories and generate folders & notebooks
for category, subcategories in merch_structure.items():
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)

    # Create category notebook with links to subcategories
    category_notebook = os.path.join(category_path, f"{category}.ipynb")
    category_content = f"# {category}\n\n## Subcategories:\n"
    
    # Handle subcategories
    if isinstance(subcategories, dict):
        for subcat, items in subcategories.items():
            subcat_path = os.path.join(category_path, subcat)
            os.makedirs(subcat_path, exist_ok=True)
            
            # Create subcategory notebook
            subcat_notebook = os.path.join(subcat_path, f"{subcat}.ipynb")
            subcat_content = f"# {subcat}\n\n## Merchandise Items:\n"
            
            for item in items:
                item_notebook = os.path.join(subcat_path, f"{item}.ipynb")
                create_notebook(item_notebook, f"# {item}\n\n(Describe the design here.)")
                subcat_content += f"- [{item}](./{item.replace(' ', '%20')}.ipynb)\n"
            
            create_notebook(subcat_notebook, subcat_content)
            category_content += f"- [{subcat}](./{subcat}/{subcat.replace(' ', '%20')}.ipynb)\n"
    
    else:  # Handle best sellers/custom merch
        for item in subcategories:
            item_notebook = os.path.join(category_path, f"{item}.ipynb")
            create_notebook(item_notebook, f"# {item}\n\n(Describe the design here.)")
            category_content += f"- [{item}](./{item.replace(' ', '%20')}.ipynb)\n"
    
    create_notebook(category_notebook, category_content)

print("✅ Jupyter Notebooks and Directories Created Successfully!")
```

```python

```