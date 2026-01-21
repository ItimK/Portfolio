#!/usr/bin/env python3
import os
import re

# Your GitHub repository info
GITHUB_USER = "ItimK"
REPO_NAME = "Portfolio"
RELEASE_TAG = "v1.0.0"

# Base URL for your release
BASE_URL = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/releases/download/{RELEASE_TAG}"

# Video mappings: old path -> new filename
VIDEO_MAPPINGS = {
    "Videos/HomePageBG.mp4": "HomePageBG.mp4",
    "Videos/ArnoldPresetsManager_Demo.mp4": "ArnoldPresetsManager_Demo.mp4",
    "Videos/ArnoldSettingCapture_Demo.mp4": "ArnoldSettingCapture_Demo.mp4",
    "Videos/ChocolateShop_Breakdown.mp4": "ChocolateShop_Breakdown.mp4",
    "Videos/SilentHelper.mp4": "SilentHelper.mp4",
    "Videos/SketchToRender_Demo.mp4": "SketchToRender_Demo.mp4",
    "Videos/StyleTransfer_Demo.mp4": "StyleTransfer_Demo.mp4",
    "Videos/TheMarbleTemple.mp4": "TheMarbleTemple.mp4",
    "Videos/WaterDropAutomaton.mp4": "WaterDropAutomaton.mp4",
    "Videos/WinterScatterTool.mp4": "WinterScatterTool.mp4",
    "Videos/WoodlandGrave.mp4": "WoodlandGrave.mp4",
    "Videos/VFX775/VFX775_GS_01.mp4": "VFX775_GS_01.mp4",
    "Videos/VFX775/VFX775_Tree_01.mp4": "VFX775_Tree_01.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_01.mp4": "VFX775_W02_GSTransfer_01.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_02.mp4": "VFX775_W02_GSTransfer_02.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_03.mp4": "VFX775_W02_GSTransfer_03.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_04.mp4": "VFX775_W02_GSTransfer_04.mp4",
    "Videos/W26_SANM560/W26_SANM560_AIOutput_01.mp4": "W26_SANM560_AIOutput_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_AIOutput_02.mp4": "W26_SANM560_AIOutput_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_Layout.mp4": "W26_SANM560_Layout.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_01.mp4": "W26_SANM560_Ref_FX_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_02.mp4": "W26_SANM560_Ref_FX_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_03.mp4": "W26_SANM560_Ref_FX_03.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_04.mp4": "W26_SANM560_Ref_FX_04.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_05.mp4": "W26_SANM560_Ref_FX_05.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_06.mp4": "W26_SANM560_Ref_FX_06.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_LO_01.mp4": "W26_SANM560_Ref_LO_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_LO_02.mp4": "W26_SANM560_Ref_LO_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_W02_S06_01.mp4": "W26_SANM560_W02_S06_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_W02_S06_02.mp4": "W26_SANM560_W02_S06_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_W02_Video.mp4": "W26_SANM560_W02_Video.mp4",
}

def update_html_file(filepath):
    """Update video URLs in an HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace each video path
    for old_path, new_filename in VIDEO_MAPPINGS.items():
        new_url = f"{BASE_URL}/{new_filename}"
        content = content.replace(old_path, new_url)
    
    # Only write if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
        return True
    else:
        print(f"⏭️  No changes: {filepath}")
        return False

def main():
    """Find and update all HTML files"""
    html_files = []
    
    # Find all HTML files in current directory
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            html_files.append(filename)
    
    if not html_files:
        print("❌ No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML files\n")
    
    updated_count = 0
    for html_file in html_files:
        if update_html_file(html_file):
            updated_count += 1
    
    print(f"\n✨ Done! Updated {updated_count} files")

if __name__ == "__main__":
    main()