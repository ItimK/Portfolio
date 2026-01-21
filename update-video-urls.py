cat > update-video-urls.py << 'EOF'
#!/usr/bin/env python3
import os

GITHUB_USER = "ItimK"
REPO_NAME = "Portfolio"
RELEASE_TAG = "v1.0.0"
BASE_URL = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/releases/download/{RELEASE_TAG}"

VIDEO_MAPPINGS = {
    "Videos/HomePageBG.mp4": f"{BASE_URL}/HomePageBG.mp4",
    "Videos/ArnoldPresetsManager_Demo.mp4": f"{BASE_URL}/ArnoldPresetsManager_Demo.mp4",
    "Videos/ArnoldSettingCapture_Demo.mp4": f"{BASE_URL}/ArnoldSettingCapture_Demo.mp4",
    "Videos/ChocolateShop_Breakdown.mp4": f"{BASE_URL}/ChocolateShop_Breakdown.mp4",
    "Videos/SilentHelper.mp4": f"{BASE_URL}/SilentHelper.mp4",
    "Videos/SketchToRender_Demo.mp4": f"{BASE_URL}/SketchToRender_Demo.mp4",
    "Videos/StyleTransfer_Demo.mp4": f"{BASE_URL}/StyleTransfer_Demo.mp4",
    "Videos/TheMarbleTemple.mp4": f"{BASE_URL}/TheMarbleTemple.mp4",
    "Videos/WaterDropAutomaton.mp4": f"{BASE_URL}/WaterDropAutomaton.mp4",
    "Videos/WinterScatterTool.mp4": f"{BASE_URL}/WinterScatterTool.mp4",
    "Videos/WoodlandGrave.mp4": f"{BASE_URL}/WoodlandGrave.mp4",
    "Videos/VFX775/VFX775_GS_01.mp4": f"{BASE_URL}/VFX775_GS_01.mp4",
    "Videos/VFX775/VFX775_Tree_01.mp4": f"{BASE_URL}/VFX775_Tree_01.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_01.mp4": f"{BASE_URL}/VFX775_W02_GSTransfer_01.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_02.mp4": f"{BASE_URL}/VFX775_W02_GSTransfer_02.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_03.mp4": f"{BASE_URL}/VFX775_W02_GSTransfer_03.mp4",
    "Videos/VFX775/VFX775_W02_GSTransfer_04.mp4": f"{BASE_URL}/VFX775_W02_GSTransfer_04.mp4",
    "Videos/W26_SANM560/W26_SANM560_AIOutput_01.mp4": f"{BASE_URL}/W26_SANM560_AIOutput_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_AIOutput_02.mp4": f"{BASE_URL}/W26_SANM560_AIOutput_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_Layout.mp4": f"{BASE_URL}/W26_SANM560_Layout.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_01.mp4": f"{BASE_URL}/W26_SANM560_Ref_FX_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_02.mp4": f"{BASE_URL}/W26_SANM560_Ref_FX_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_03.mp4": f"{BASE_URL}/W26_SANM560_Ref_FX_03.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_04.mp4": f"{BASE_URL}/W26_SANM560_Ref_FX_04.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_05.mp4": f"{BASE_URL}/W26_SANM560_Ref_FX_05.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_FX_06.mp4": f"{BASE_URL}/W26_SANM560_Ref_FX_06.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_LO_01.mp4": f"{BASE_URL}/W26_SANM560_Ref_LO_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_Ref_LO_02.mp4": f"{BASE_URL}/W26_SANM560_Ref_LO_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_W02_S06_01.mp4": f"{BASE_URL}/W26_SANM560_W02_S06_01.mp4",
    "Videos/W26_SANM560/W26_SANM560_W02_S06_02.mp4": f"{BASE_URL}/W26_SANM560_W02_S06_02.mp4",
    "Videos/W26_SANM560/W26_SANM560_W02_Video.mp4": f"{BASE_URL}/W26_SANM560_W02_Video.mp4",
}

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in VIDEO_MAPPINGS.items():
        content = content.replace(old, new)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
        return True
    else:
        print(f"⏭️  No changes: {filepath}")
        return False

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    count = sum(update_html_file(f) for f in files)
    print(f"\n✨ Updated {count} files")

if __name__ == "__main__":
    main()
EOF

# Make it executable
chmod +x update-video-urls.py

# Run it
python3 update-video-urls.py