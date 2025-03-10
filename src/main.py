import os
import shutil
import re

from generate_page import generate_page


def copy_directory(src, dest):
    """
    Recursively copies all contents from src directory to dest directory.
    First, it deletes all contents of dest to ensure a clean copy.
    """
    # Ensure the source directory exists
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
        return
    
    # Remove destination directory if it exists
    if os.path.exists(dest):
        print(f"Removing existing directory: {dest}")
        shutil.rmtree(dest)
    
    # Create the destination directory
    os.makedirs(dest, exist_ok=True)
    print(f"Created directory: {dest}")
    
    # Recursively copy contents
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        
        if os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            os.makedirs(dest_path, exist_ok=True)
            copy_directory(src_path, dest_path)
        else:
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)

def main():
    src_dir = "static"
    dest_dir = "public"
    content_file = "content/index.md"
    template_file = "template.html"
    output_file = "public/index.html"
    
    # Clean public directory and copy static files
    copy_directory(src_dir, dest_dir)
    
    # Generate main page
    generate_page(content_file, template_file, output_file)
    
    print("Site generation complete.")

if __name__ == "__main__":
    main()