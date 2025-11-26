---
title: Config Script
source_file: Hawk_Eye_Dev_Notebooks copy/Rap_Merch/Config_Script.ipynb
---

```python
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

# Define base directory for Rap Merch
base_dir = os.path.expanduser("~/Notebooks/Omniversal-Server/Hawk_Eye_Dev_Notebooks/Rap_Merch")

# Ensure base directory exists
os.makedirs(base_dir, exist_ok=True)

# Debugging information
print(f"📂 Base directory set to: {base_dir}")
print(f"Current working directory: {os.getcwd()}")
print(f"Does base directory exist? {'✅ Yes' if os.path.exists(base_dir) else '❌ No'}")

# Define the primary store structure
store_structure = {
    "Merchandise_Categories": ["Album-Inspired_Collections", "Limited_Edition_Drops", "Best_Sellers", "Custom_Merch_Creator"],
    "Product_Concepts": ["T-Shirts", "Hoodies", "Hats", "Accessories", "Posters"],
    "Website_Layout_and_Pages": ["Home_Page", "Category_Pages", "Product_Detail_Pages", "Cart_and_Checkout"],
    "Amazon_Integration_and_Listing_Strategy": ["Print_on_Demand_Setup", "SEO_and_Keyword_Strategy", "Pricing_and_Profit_Margins", "Marketing_and_Promotion"],
    "Marketing_Strategy": ["Social_Media_Campaigns", "Influencer_Collaborations", "Email_Marketing", "Paid_Ads"]
}

# Define detailed merchandise collections
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
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Ensure folder exists
    with open(filepath, 'w') as f:
        nbformat.write(nb, f)

# Create primary store structure directories & notebooks
for main_category, subcategories in store_structure.items():
    category_path = os.path.join(base_dir, main_category)
    os.makedirs(category_path, exist_ok=True)
    
    for subcategory in subcategories:
        subcategory_path = os.path.join(category_path, subcategory)
        os.makedirs(subcategory_path, exist_ok=True)
        
        # Create a notebook inside each subcategory
        notebook_path = os.path.join(subcategory_path, f"{subcategory}.ipynb")
        create_notebook(notebook_path, f"# 📂 {subcategory.replace('_', ' ')}\n\n(Add content here)")

# Create Hawk_Merch.ipynb with links to all sections
expanded_notebook_path = os.path.join(base_dir, "Hawk_Merch.ipynb")
expanded_content = "# 🎤 Hawk Eye The Rapper - Merchandise Store (Expanded Version)\n\n"

for main_category, subcategories in store_structure.items():
    expanded_content += f"## {main_category.replace('_', ' ')}\n"
    for subcategory in subcategories:
        subcategory_path = os.path.join(main_category, subcategory, f"{subcategory}.ipynb")
        expanded_content += f"- [{subcategory.replace('_', ' ')}]({subcategory_path})\n"
    expanded_content += "\n"

create_notebook(expanded_notebook_path, expanded_content)

# Create Original_Hawk.ipynb with a link to the expanded version
original_notebook_path = os.path.join(base_dir, "Original_Hawk.ipynb")
original_content = "# 🎤 Hawk Eye The Rapper - Merchandise Store (Original Version)\n\n"
original_content += "🔗 **[View Expanded Version](Hawk_Merch.ipynb)**\n\n"
original_content += "## Merchandise Store Planning Contents\n\n"

for main_category in store_structure.keys():
    original_content += f"- [{main_category.replace('_', ' ')}](Hawk_Merch.ipynb)\n"

create_notebook(original_notebook_path, original_content)

# Generate detailed merchandise structure inside "Merchandise_Categories"
merch_base_dir = os.path.join(base_dir, "Merchandise_Categories")

for category, subcategories in merch_structure.items():
    category_path = os.path.join(merch_base_dir, category)
    os.makedirs(category_path, exist_ok=True)

    # Create category notebook with links to subcategories
    category_notebook = os.path.join(category_path, f"{category}.ipynb")
    category_content = f"# {category}\n\n## Subcategories:\n"

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

    else:
        for item in subcategories:
            item_notebook = os.path.join(category_path, f"{item}.ipynb")
            create_notebook(item_notebook, f"# {item}\n\n(Describe the design here.)")
            category_content += f"- [{item}](./{item.replace(' ', '%20')}.ipynb)\n"

    create_notebook(category_notebook, category_content)

print("✅ Jupyter Notebooks and Directories Created Successfully!")
```

```python

```