import os

# Path to your repository
base_path = r"C:\Users\ajits\OneDrive\Desktop\LLM\1-Langchain"

def rename_with_leading_zero(path):
    for item in os.listdir(path):
        old_item_path = os.path.join(path, item)

        # Only process items that start with a single digit followed by "-"
        if item[0].isdigit() and (len(item.split('-')[0]) == 1):
            new_name = "0" + item
            new_item_path = os.path.join(path, new_name)
            os.rename(old_item_path, new_item_path)
            print(f"Renamed: {old_item_path} → {new_item_path}")
            old_item_path = new_item_path  # Update path in case we need recursion

        # If it's a folder, recurse into it
        if os.path.isdir(old_item_path):
            rename_with_leading_zero(old_item_path)

rename_with_leading_zero(base_path)
