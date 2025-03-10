import os
import re
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    """
    Extracts the h1 title from markdown content.
    """
    match = re.search(r'^# (.+)', markdown, re.MULTILINE)
    if not match:
        raise ValueError("No H1 title found in markdown.")
    return match.group(1).strip()

def generate_page(from_path, template_path, dest_path):
    """
    Generates an HTML page from a markdown file using a template.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    
    # Read template file
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Convert markdown to HTML (assuming markdown_to_html_node function exists)
    html_content = markdown_to_html_node(markdown_content).to_html()
    
    # Replace placeholders
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write final HTML
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Page generated at {dest_path}")