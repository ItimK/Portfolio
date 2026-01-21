#!/usr/bin/env python3
import os
import re

GITHUB_USER = "ItimK"
REPO_NAME = "Portfolio"
RELEASE_TAG = "v1.0.0"

# Old GitHub Releases URL
OLD_BASE = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/releases/download/{RELEASE_TAG}"

# New jsDelivr CDN URL (much better for mobile)
NEW_BASE = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}@{RELEASE_TAG}"

def update_html_file(filepath):
    """Replace GitHub Releases URLs with jsDelivr CDN URLs"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace the base URL
    content = content.replace(OLD_BASE, NEW_BASE)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
        return True
    else:
        print(f"⏭️  No changes: {filepath}")
        return False

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if not html_files:
        print("❌ No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML files\n")
    print(f"Replacing:\n  {OLD_BASE}")
    print(f"With:\n  {NEW_BASE}\n")
    
    updated_count = 0
    for html_file in html_files:
        if update_html_file(html_file):
            updated_count += 1
    
    print(f"\n✨ Done! Updated {updated_count} files")

if __name__ == "__main__":
    main()