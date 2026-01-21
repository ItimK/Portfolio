#!/usr/bin/env python3
import os
import re

def update_video_tags(content):
    """Add mobile-friendly attributes to video tags"""
    
    # Pattern to find <video> tags
    video_pattern = r'<video([^>]*)>'
    
    def add_attributes(match):
        attrs = match.group(1)
        
        # Add webkit-playsinline if not present
        if 'webkit-playsinline' not in attrs.lower():
            attrs += ' webkit-playsinline'
        
        # Add preload="auto" if not present
        if 'preload' not in attrs.lower():
            attrs += ' preload="auto"'
        
        # Ensure playsinline is present
        if 'playsinline' not in attrs.lower():
            attrs += ' playsinline'
            
        return f'<video{attrs}>'
    
    content = re.sub(video_pattern, add_attributes, content)
    
    return content

def update_html_file(filepath):
    """Update video tags in an HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    content = update_video_tags(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
        return True
    else:
        print(f"⏭️  No changes needed: {filepath}")
        return False

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if not html_files:
        print("❌ No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML files\n")
    
    updated_count = 0
    for html_file in html_files:
        if update_html_file(html_file):
            updated_count += 1
    
    print(f"\n✨ Done! Updated {updated_count} files")
    print("\nNext steps:")
    print("1. git add *.html")
    print("2. git commit -m 'Add mobile video attributes'")
    print("3. git push origin main")

if __name__ == "__main__":
    main()