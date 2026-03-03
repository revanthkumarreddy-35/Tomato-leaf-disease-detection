"""
Cross-Platform Setup & Training Script
Works on: Windows 10+, Linux, macOS
"""

import subprocess
import sys
import os
import platform
from pathlib import Path


def install_dependencies():
    """Install all required Python packages."""
    print("📦 Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed!\n")


def check_environment():
    """Check system environment and GPU availability."""
    print("="*60)
    print("🖥️  SYSTEM INFORMATION")
    print("="*60)
    print(f"   OS:      {platform.system()} {platform.release()}")
    print(f"   Python:  {sys.version.split()[0]}")
    print(f"   Arch:    {platform.machine()}")

    try:
        import torch
        print(f"   PyTorch: {torch.__version__}")
        if torch.cuda.is_available():
            print(f"   GPU:     ✅ {torch.cuda.get_device_name(0)}")
            print(f"   CUDA:    {torch.version.cuda}")
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            print(f"   GPU:     ✅ Apple Silicon (MPS)")
        else:
            print(f"   GPU:     ⚠️  Not available (will use CPU)")
    except ImportError:
        print("   PyTorch: ❌ Not installed — run: pip install -r requirements.txt")
        return False

    try:
        import ultralytics
        print(f"   YOLO:    {ultralytics.__version__}")
    except ImportError:
        print("   YOLO:    ❌ Not installed — run: pip install -r requirements.txt")
        return False

    print()
    return True


def check_dataset():
    """Verify dataset exists and show stats."""
    dataset_path = Path("./Tomato-Leaf-Disease-63")
    print("="*60)
    print("📂 DATASET CHECK")
    print("="*60)

    if not dataset_path.exists():
        print("   ❌ Dataset folder not found: Tomato-Leaf-Disease-63/")
        print("   📥 Download it from:")
        print("      https://www.kaggle.com/datasets/kpoviesistphane/tomato-leaf-disease-detection")
        print("   📁 Extract it so the structure is:")
        print("      Tomato-Leaf-Disease-63/")
        print("        ├── train/images/")
        print("        ├── valid/images/")
        print("        └── test/images/")
        return False

    for split in ["train", "valid", "test"]:
        img_dir = dataset_path / split / "images"
        if img_dir.exists():
            count = len(list(img_dir.iterdir()))
            print(f"   ✅ {split:>5} images: {count}")
        else:
            print(f"   ❌ {split:>5} images: NOT FOUND")
            return False

    print()
    return True


def main():
    print("\n🍅 Tomato Leaf Disease Detection — Setup & Train\n")

    if not check_environment():
        print("\n⚠️  Missing dependencies. Installing now...")
        install_dependencies()
        if not check_environment():
            print("❌ Setup failed. Please install manually: pip install -r requirements.txt")
            return

    if not check_dataset():
        print("\n❌ Cannot proceed without dataset. See instructions above.")
        return

    print("✅ Everything looks good! You can now train the model:\n")
    print("   python train_yolov8.py")
    print("   — or —")
    print("   jupyter notebook train_model.ipynb\n")


if __name__ == "__main__":
    main()
