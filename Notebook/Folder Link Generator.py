import pyperclip

def generate_folder_link_and_copy(folder_path, link_text="Open Project Folder"):
    """
    Generate an HTML link for a relative folder path, print it, and copy it to the clipboard.

    Args:
        folder_path (str): The relative path to the folder (e.g., "Projects/Day 32").
        link_text (str): The text to display for the link.

    Returns:
        None: Prints the link and copies it to the clipboard.
    """
    # Replace backslashes with forward slashes for compatibility
    formatted_path = folder_path.replace("\\", "/")
    # Escape spaces and other URL-unsafe characters
    url_path = f"./{formatted_path}".replace(" ", "%20")
    # Generate Markdown-compatible HTML link
    html_link = f'<a href="{url_path}" target="_blank">{link_text}</a>'
    
    # Print the link in the terminal
    print(f"Generated link: {html_link}")
    
    # Copy the link to the clipboard
    pyperclip.copy(html_link)
    print("The link has been copied to the clipboard.")

generate_folder_link_and_copy(r"Projects\24- Automated Birthday Wisher (Day 32)")

