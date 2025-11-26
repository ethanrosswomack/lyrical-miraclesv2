---
title: Config Script
source_file: Hawk_Eye_Dev_Notebooks copy/Hawk_Eye_Store/Config/Config_Script.ipynb
---

```python
import os
import nbformat

# Define base directory
base_path = os.getcwd()  # This ensures it runs inside your Jupyter Notebook's working directory

# Define directory structure
store_structure = {
    "Merchandise_Categories": ["Album-Inspired_Collections", "Limited_Edition_Drops", "Best_Sellers", "Custom_Merch_Creator"],
    "Product_Concepts": ["T-Shirts", "Hoodies", "Hats", "Accessories", "Posters"],
    "Website_Layout_and_Pages": ["Home_Page", "Category_Pages", "Product_Detail_Pages", "Cart_and_Checkout"],
    "Amazon_Integration_and_Listing_Strategy": ["Print_on_Demand_Setup", "SEO_and_Keyword_Strategy", "Pricing_and_Profit_Margins", "Marketing_and_Promotion"],
    "Marketing_Strategy": ["Social_Media_Campaigns", "Influencer_Collaborations", "Email_Marketing", "Paid_Ads"]
}

# Function to create directories and notebooks
def create_structure(base_path, structure):
    for main_category, subcategories in structure.items():
        main_category_path = os.path.join(base_path, main_category)
        os.makedirs(main_category_path, exist_ok=True)
        
        for subcategory in subcategories:
            subcategory_path = os.path.join(main_category_path, subcategory)
            os.makedirs(subcategory_path, exist_ok=True)
            
            # Create an empty Jupyter notebook in each subcategory
            notebook_path = os.path.join(subcategory_path, f"{subcategory}.ipynb")
            notebook = nbformat.v4.new_notebook()
            notebook.cells.append(nbformat.v4.new_markdown_cell(f"# 📂 {subcategory.replace('_', ' ')}\n\n(Add content here)"))
            
            with open(notebook_path, "w") as nb_file:
                nbformat.write(notebook, nb_file)

# Run the function to create directories and notebooks
create_structure(base_path, store_structure)

# Create Hawk_Merch.ipynb with links to all sections
expanded_notebook_path = os.path.join(base_path, "Hawk_Merch.ipynb")
expanded_content = "# 🎤 Hawk Eye The Rapper - Merchandise Store (Expanded Version)\n\n"

for main_category, subcategories in store_structure.items():
    expanded_content += f"## {main_category.replace('_', ' ')}\n"
    for subcategory in subcategories:
        subcategory_path = os.path.join(main_category, subcategory, f"{subcategory}.ipynb")
        expanded_content += f"- [{subcategory.replace('_', ' ')}]({subcategory_path})\n"
    expanded_content += "\n"

expanded_notebook = nbformat.v4.new_notebook()
expanded_notebook.cells.append(nbformat.v4.new_markdown_cell(expanded_content))

with open(expanded_notebook_path, "w") as nb_file:
    nbformat.write(expanded_notebook, nb_file)

# Create Original_Hawk.ipynb with a link to the expanded version
original_notebook_path = os.path.join(base_path, "Original_Hawk.ipynb")
original_content = "# 🎤 Hawk Eye The Rapper - Merchandise Store (Original Version)\n\n"
original_content += "🔗 **[View Expanded Version](Hawk_Merch.ipynb)**\n\n"
original_content += "## Merchandise Store Planning Contents\n\n"

for main_category in store_structure.keys():
    original_content += f"- [{main_category.replace('_', ' ')}](Hawk_Merch.ipynb)\n"

original_notebook = nbformat.v4.new_notebook()
original_notebook.cells.append(nbformat.v4.new_markdown_cell(original_content))

with open(original_notebook_path, "w") as nb_file:
    nbformat.write(original_notebook, nb_file)

# Output Success Message
print("✅ Directory structure and notebooks successfully created!")
print(f"📂 Hawk_Merch.ipynb and Original_Hawk.ipynb are now available in: {base_path}")
```

```python

```