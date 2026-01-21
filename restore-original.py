#!/usr/bin/env python3
import os
import re

GITHUB_USER = "ItimK"
REPO_NAME = "Portfolio"
RELEASE_TAG = "v1.0.0"

# All possible GitHub URLs to remove
RELEASES_URL = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/releases/download/{RELEASE_TAG}/"
JSDELIVR_URL = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}@{RELEASE_TAG}"
MEDIA_URL = f"https://media.githubusercontent.com/media/{GITHUB_USER}/{REPO_NAME}/main"

VIDEO_MAPPINGS = {
    "HomePageBG.mp4": "Videos/HomePageBG.mp4",
    "ArnoldPresetsManager_Demo.mp4": "Videos/ArnoldPresetsManager_Demo.mp4",
    "ArnoldSettingCapture_Demo.mp4": "Videos/ArnoldSettingCapture_Demo.mp4",
    "ChocolateShop_Breakdown.mp4": "Videos/ChocolateShop_Breakdown.mp4",
    "SilentHelper.mp4": "Videos/SilentHelper.mp4",
    "SketchToRender_Demo.mp4": "Videos/SketchToRender_Demo.mp4",
    "StyleTransfer_Demo.mp4": "Videos/StyleTransfer_Demo.mp4",
    "TheMarbleTemple.mp4": "Videos/TheMarbleTemple.mp4",
    "WaterDropAutomaton.mp4": "Videos/WaterDropAutomaton.mp4",
    "WinterScatterTool.mp4": "Videos/WinterScatterTool.mp4",
    "WoodlandGrave.mp4": "Videos/WoodlandGrave.mp4",
    "VFX775_GS_01.mp4": "Videos/VFX775/VFX775_GS_01.mp4",
    "VFX775_Tree_01.mp4": "Videos/VFX775/VFX775_Tree_01.mp4",
    "VFX775_W02_GSTransfer_01.mp4": "Videos/VFX775/VFX775_W02_GSTransfer_01.mp4",
    "VFX775_W02_GSTransfer_02.mp4": "Videos/VFX775/VFX775_W02_GSTransfer_02.mp4",
    "VFX775_W02_GSTransfer_03.mp4": "Videos/VFX775/VFX775_W02_GSTransfer_03.mp4",
    "VFX775_W02_GSTransfer_04.mp4": "Videos/VFX775/VFX775_W02_GSTransfer_04.mp4",
    "W26_SANM560_AIOutput_01.mp4": "Videos/W26_SANM560/W26_SANM560_AIOutput_01.mp4",
    "W26_SANM560_AIOutput_02.mp4": "Videos/W26_SANM560/W26_SANM560_AIOutput_02.mp4",
    "W26_SANM560_Layout.mp4": "Videos/W26_SANM560/W26_SANM560_Layout.mp4",
    "W26_SANM560_Ref_FX_01.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_FX_01.mp4",
    "W26_SANM560_Ref_FX_02.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_FX_02.mp4",
    "W26_SANM560_Ref_FX_03.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_FX_03.mp4",
    "W26_SANM560_Ref_FX_04.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_FX_04.mp4",
    "W26_SANM560_Ref_FX_05.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_FX_05.mp4",
    "W26_SANM560_Ref_FX_06.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_FX_06.mp4",
    "W26_SANM560_Ref_LO_01.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_LO_01.mp4",
    "W26_SANM560_Ref_LO_02.mp4": "Videos/W26_SANM560/W26_SANM560_Ref_LO_02.mp4",
    "W26_SANM560_W02_S06_01.mp4": "Videos/W26_SANM560/W26_SANM560_W02_S06_01.mp4",
    "W26_SANM560_W02_S06_02.mp4": "Videos/W26_SANM560/W26_SANM560_W02_S06_02.mp4",
    "W26_SANM560_W02_Video.mp4": "Videos/W26_SANM560/W26_SANM560_W02_Video.mp4",
}

def clean_video_attributes(content):
    """Remove extra attributes added by fix-mobile-videos.py"""
    # Remove webkit-playsinline
    content = re.sub(r'\s+webkit-playsinline', '', content)
    # Remove preload="auto"
    content = re.sub(r'\s+preload="auto"', '', content)
    return content

def update_html_file(filepath):
    """Restore to original state"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace all GitHub URLs with local paths
    for release_filename, local_path in VIDEO_MAPPINGS.items():
        # Try all possible URL formats
        content = content.replace(f"{RELEASES_URL}{release_filename}", local_path)
        content = content.replace(f"{JSDELIVR_URL}/{release_filename}", local_path)
        content = content.replace(f"{MEDIA_URL}/Videos/{release_filename}", local_path)
    
    # Remove extra attributes
    content = clean_video_attributes(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Restored: {filepath}")
        return True
    else:
        print(f"⏭️  Already clean: {filepath}")
        return False

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if not html_files:
        print("❌ No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML files\n")
    print("Restoring to original state...\n")
    
    updated_count = 0
    for html_file in html_files:
        if update_html_file(html_file):
            updated_count += 1
    
    print(f"\n✨ Done! Restored {updated_count} files to original state")
    print("\nVideos are back to: Videos/...paths")
    print("Extra attributes removed")

if __name__ == "__main__":
    main()