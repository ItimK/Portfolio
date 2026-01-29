#!/usr/bin/env python3
"""
HTML URL Update Script
Updates all HTML files to use new R2 video URLs instead of GitHub releases
"""

import os
import sys
import re
from pathlib import Path

# Configuration
R2_PUBLIC_URL = 'https://pub-e1b6174ab96b483fac33c4dd503ce079.r2.dev'
GITHUB_RELEASE_PATTERN = r'https://github\.com/ItimK/Portfolio/releases/download/v1\.0\.0/'

def find_html_files(directory):
    """Find all HTML files in directory and subdirectories"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories and common non-source directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'dist', 'build']]
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    return html_files

def update_video_urls(content):
    """Replace GitHub release URLs with R2 URLs"""
    # Pattern matches GitHub release video URLs
    pattern = r'https://github\.com/ItimK/Portfolio/releases/download/v1\.0\.0/([^"\'>\s]+)'
    
    def replace_url(match):
        filename = match.group(1)
        
        # Check if filename starts with folder prefixes that need folder structure
        if filename.startswith('W26_SANM560'):
            # Add W26_SANM560/ folder prefix
            new_url = f"{R2_PUBLIC_URL}/W26_SANM560/{filename}"
        elif filename.startswith('VFX775'):
            # Add VFX775/ folder prefix
            new_url = f"{R2_PUBLIC_URL}/VFX775/{filename}"
        else:
            # Root level video
            new_url = f"{R2_PUBLIC_URL}/{filename}"
        
        return new_url
    
    updated_content = re.sub(pattern, replace_url, content)
    return updated_content

def count_replacements(content, updated_content):
    """Count how many URLs were replaced"""
    original_count = len(re.findall(GITHUB_RELEASE_PATTERN, content))
    updated_count = len(re.findall(GITHUB_RELEASE_PATTERN, updated_content))
    return original_count - updated_count

def update_html_file(filepath, dry_run=False):
    """Update a single HTML file with new URLs"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = update_video_urls(content)
        replacements = count_replacements(content, updated_content)
        
        if replacements > 0:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✓ {filepath}: Updated {replacements} URL(s)")
            else:
                print(f"  {filepath}: Would update {replacements} URL(s)")
            return replacements
        else:
            print(f"  {filepath}: No GitHub release URLs found")
            return 0
    
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_html_urls.py <path_to_portfolio_directory> [--dry-run]")
        print("\nExample:")
        print("  python update_html_urls.py /Users/yourname/Portfolio")
        print("  python update_html_urls.py /Users/yourname/Portfolio --dry-run")
        print("\nOptions:")
        print("  --dry-run    Preview changes without modifying files")
        sys.exit(1)
    
    portfolio_dir = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    if not os.path.isdir(portfolio_dir):
        print(f"Error: Directory not found: {portfolio_dir}")
        sys.exit(1)
    
    print("=" * 60)
    print("HTML URL Update Script")
    if dry_run:
        print("MODE: DRY RUN (no files will be modified)")
    print("=" * 60)
    print(f"Portfolio directory: {portfolio_dir}")
    print(f"Replacing: {GITHUB_RELEASE_PATTERN}")
    print(f"With: {R2_PUBLIC_URL}/")
    print("=" * 60)
    
    # Find all HTML files
    print("\nSearching for HTML files...")
    html_files = find_html_files(portfolio_dir)
    
    if not html_files:
        print("No HTML files found in the directory!")
        sys.exit(1)
    
    print(f"Found {len(html_files)} HTML files\n")
    
    if not dry_run:
        response = input("Proceed with updating files? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("Update cancelled.")
            sys.exit(0)
    
    # Update files
    print("\nProcessing files...")
    total_replacements = 0
    files_updated = 0
    
    for html_file in html_files:
        replacements = update_html_file(html_file, dry_run)
        if replacements > 0:
            files_updated += 1
            total_replacements += replacements
    
    # Summary
    print("\n" + "=" * 60)
    print("Update Summary")
    print("=" * 60)
    if dry_run:
        print(f"Files that would be updated: {files_updated}")
        print(f"Total URLs that would be replaced: {total_replacements}")
        print("\nRun without --dry-run to apply changes")
    else:
        print(f"✓ Files updated: {files_updated}")
        print(f"✓ Total URLs replaced: {total_replacements}")
        print("\nNext steps:")
        print("1. Test your website locally")
        print("2. Verify videos load correctly from R2")
        print("3. Commit and push changes to GitHub")
        print("4. Check your live site on GitHub Pages")
    print("=" * 60)

if __name__ == '__main__':
    main()