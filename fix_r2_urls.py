#!/usr/bin/env python3
"""
Fix R2 URLs Script
Fixes R2 URLs to include proper folder structure for W26_SANM560 and VFX775 videos
"""

import os
import sys
import re
from pathlib import Path

# Configuration
R2_PUBLIC_URL = 'https://pub-e1b6174ab96b483fac33c4dd503ce079.r2.dev'

def find_html_files(directory):
    """Find all HTML files in directory and subdirectories"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'dist', 'build']]
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    return html_files

def fix_r2_urls(content):
    """Fix R2 URLs to include proper folder structure"""
    
    # Pattern 1: Fix W26_SANM560 videos that are missing folder prefix
    # Matches: .../W26_SANM560_xxx.mp4 (without /W26_SANM560/ folder)
    # Changes to: .../W26_SANM560/W26_SANM560_xxx.mp4
    pattern1 = rf'{re.escape(R2_PUBLIC_URL)}/(?!W26_SANM560/)(W26_SANM560[^"\'>\s]+)'
    content = re.sub(pattern1, f'{R2_PUBLIC_URL}/W26_SANM560/\\1', content)
    
    # Pattern 2: Fix VFX775 videos that are missing folder prefix
    # Matches: .../VFX775_xxx.mp4 (without /VFX775/ folder)
    # Changes to: .../VFX775/VFX775_xxx.mp4
    pattern2 = rf'{re.escape(R2_PUBLIC_URL)}/(?!VFX775/)(VFX775[^"\'>\s]+)'
    content = re.sub(pattern2, f'{R2_PUBLIC_URL}/VFX775/\\1', content)
    
    return content

def count_fixes(content, fixed_content):
    """Count how many URLs were fixed"""
    # Count W26_SANM560 fixes
    w26_before = len(re.findall(rf'{re.escape(R2_PUBLIC_URL)}/(?!W26_SANM560/)W26_SANM560', content))
    w26_after = len(re.findall(rf'{re.escape(R2_PUBLIC_URL)}/(?!W26_SANM560/)W26_SANM560', fixed_content))
    
    # Count VFX775 fixes
    vfx_before = len(re.findall(rf'{re.escape(R2_PUBLIC_URL)}/(?!VFX775/)VFX775', content))
    vfx_after = len(re.findall(rf'{re.escape(R2_PUBLIC_URL)}/(?!VFX775/)VFX775', fixed_content))
    
    return (w26_before - w26_after) + (vfx_before - vfx_after)

def fix_html_file(filepath, dry_run=False):
    """Fix a single HTML file with correct R2 URLs"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixed_content = fix_r2_urls(content)
        fixes = count_fixes(content, fixed_content)
        
        if fixes > 0:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"✓ {filepath}: Fixed {fixes} URL(s)")
            else:
                print(f"  {filepath}: Would fix {fixes} URL(s)")
            return fixes
        else:
            print(f"  {filepath}: No URLs need fixing")
            return 0
    
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_r2_urls.py <path_to_portfolio_directory> [--dry-run]")
        print("\nExample:")
        print("  python fix_r2_urls.py /Users/yourname/PortFolioWebsite")
        print("  python fix_r2_urls.py . --dry-run")
        sys.exit(1)
    
    portfolio_dir = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    if not os.path.isdir(portfolio_dir):
        print(f"Error: Directory not found: {portfolio_dir}")
        sys.exit(1)
    
    print("=" * 60)
    print("Fix R2 URLs Script")
    if dry_run:
        print("MODE: DRY RUN (no files will be modified)")
    print("=" * 60)
    print(f"Portfolio directory: {portfolio_dir}")
    print(f"R2 URL base: {R2_PUBLIC_URL}")
    print("\nFixes:")
    print("  - .../W26_SANM560_xxx.mp4 → .../W26_SANM560/W26_SANM560_xxx.mp4")
    print("  - .../VFX775_xxx.mp4 → .../VFX775/VFX775_xxx.mp4")
    print("=" * 60)
    
    # Find all HTML files
    print("\nSearching for HTML files...")
    html_files = find_html_files(portfolio_dir)
    
    if not html_files:
        print("No HTML files found in the directory!")
        sys.exit(1)
    
    print(f"Found {len(html_files)} HTML files\n")
    
    if not dry_run:
        response = input("Proceed with fixing files? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("Update cancelled.")
            sys.exit(0)
    
    # Fix files
    print("\nProcessing files...")
    total_fixes = 0
    files_fixed = 0
    
    for html_file in html_files:
        fixes = fix_html_file(html_file, dry_run)
        if fixes > 0:
            files_fixed += 1
            total_fixes += fixes
    
    # Summary
    print("\n" + "=" * 60)
    print("Fix Summary")
    print("=" * 60)
    if dry_run:
        print(f"Files that would be fixed: {files_fixed}")
        print(f"Total URLs that would be fixed: {total_fixes}")
        print("\nRun without --dry-run to apply changes")
    else:
        print(f"✓ Files fixed: {files_fixed}")
        print(f"✓ Total URLs fixed: {total_fixes}")
        print("\nNext steps:")
        print("1. Test your website locally")
        print("2. Verify videos load correctly from R2")
        print("3. Commit and push changes to GitHub")
    print("=" * 60)

if __name__ == '__main__':
    main()
