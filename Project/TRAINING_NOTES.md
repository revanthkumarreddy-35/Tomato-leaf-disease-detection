# 📝 YOLOv8 Tomato Leaf Disease Detection — Training Notes

> **File to execute:** `train_yolov8.py`  
> **Run from folder:** The `Project/` directory  
> **Command:** `python train_yolov8.py`

---

## 🔧 Prerequisites

| Requirement | Details |
|---|---|
| Python packages | `torch`, `ultralytics`, `matplotlib` |
| Pre-trained weights | `yolov8n.pt` (must be in the `Project/` folder) |
| Dataset | `Tomato-Leaf-Disease-63/` folder with `train/`, `valid/`, `test/` subfolders |
| GPU (optional) | CUDA-compatible GPU recommended (training takes 1–4 hrs on GPU, much longer on CPU) |

---

## 📂 Dataset Structure

```
Tomato-Leaf-Disease-63/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

### 9 Disease Classes

| # | Class Name |
|---|---|
| 0 | Early_Blight |
| 1 | Healthy |
| 2 | Late_Blight |
| 3 | Leaf_Miner |
| 4 | Leaf_Mold |
| 5 | Mosaic_Virus |
| 6 | Septoria_Leaf_Spot |
| 7 | Spider_Mites |
| 8 | Yellow_Leaf_Curl_Virus |

---

## ⚙️ Training Configuration

| Parameter | Value | Notes |
|---|---|---|
| Model | YOLOv8n | Nano variant (fastest, smallest) |
| Epochs | 50 | Max training epochs |
| Image Size | 640×640 | Standard YOLO input size |
| Batch Size | 16 | Reduce to 8 if GPU runs out of memory |
| Patience | 10 | Early stopping — stops if no improvement for 10 epochs |
| Device | GPU (0) or CPU | Auto-detected |

---

## 🚀 What the Script Does (Step by Step)

1. **Checks GPU availability** — uses CUDA GPU if available, otherwise falls back to CPU
2. **Verifies dataset** — confirms `train/images`, `valid/images`, `test/images` exist and counts files
3. **Creates `data.yaml`** — YOLO config file pointing to dataset paths and class names
4. **Loads YOLOv8n** — loads pre-trained `yolov8n.pt` weights
5. **Trains the model** — runs training for up to 50 epochs with early stopping
6. **Saves results** — metrics plot + best weights saved under `runs/detect/tomato_disease_notebook/`
7. **Tests on sample images** — runs inference on first 3 test images and displays detections

---

## 📁 Output Files (After Training)

> **⚠️ IMPORTANT:** YOLO auto-increments folder names if you train multiple times:  
> `tomato_disease_notebook` → `tomato_disease_notebook2` → `tomato_disease_notebook3` → etc.  
> The code now **auto-detects the latest run folder**, so you don't need to change paths manually.

| File | Path (latest run auto-detected) |
|---|---|
| Training metrics plot | `runs/detect/tomato_disease_notebookN/results.png` |
| Best model weights | `runs/detect/tomato_disease_notebookN/weights/best.pt` |
| Last model weights | `runs/detect/tomato_disease_notebookN/weights/last.pt` |
| Confusion matrix | `runs/detect/tomato_disease_notebookN/confusion_matrix.png` |
| All training logs | `runs/detect/tomato_disease_notebookN/` |

---

## ✅ Latest Training Results (March 2, 2026 — `tomato_disease_notebook4`)

- **Duration:** 50 epochs in 3.705 hours
- **GPU:** NVIDIA GeForce RTX 2050 (4096 MiB)
- **Model:** 73 layers, 3,007,403 parameters, 8.1 GFLOPs
- **Best weights:** `runs/detect/tomato_disease_notebook4/weights/best.pt`

### Per-Class Performance

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|
| **All (overall)** | **0.951** | **0.923** | **0.971** | **0.912** |
| Early_Blight | 0.949 | 0.948 | 0.980 | 0.935 |
| Healthy | 0.892 | 0.877 | 0.936 | 0.854 |
| Late_Blight | 0.981 | 0.956 | 0.987 | 0.931 |
| Leaf_Miner | 0.959 | 0.996 | 0.988 | 0.950 |
| Leaf_Mold | 0.945 | 0.910 | 0.976 | 0.919 |
| Mosaic_Virus | 0.967 | 0.933 | 0.968 | 0.933 |
| Septoria_Leaf_Spot | 0.970 | 0.893 | 0.970 | 0.915 |
| Spider_Mites | 0.978 | 0.976 | 0.985 | 0.941 |
| Yellow_Leaf_Curl_Virus | 0.915 | 0.818 | 0.945 | 0.829 |

### Speed (per image)
| Stage | Time |
|---|---|
| Preprocess | 0.4ms |
| Inference | 4.9ms |
| Postprocess | 3.0ms |

---

## ⚠️ Common Issues & Fixes

### ❌ "Results image not found" / "Trained weights not found" (EVEN after training)
- **Cause:** The notebook was using **relative paths** (`runs/detect/...`), but the notebook's working directory was different from `Project/`, so it couldn't find the files even though they existed.
- **Fix (March 3, 2026):** Updated `project2_fixed.ipynb` to use **relative paths** with `pathlib.Path`. The notebook now auto-detects the latest training run regardless of working directory or OS.

### ❌ "Dataset not found"
- **Cause:** `Tomato-Leaf-Disease-63/` folder is missing or not in the right location.
- **Fix:** Make sure the dataset folder is inside `Project/`.

### ❌ CUDA out of memory
- **Fix:** In `train_yolov8.py`, change `batch=16` to `batch=8` (or even `batch=4`).

### ❌ Training is extremely slow
- **Cause:** Running on CPU instead of GPU.
- **Fix:** Install CUDA-compatible PyTorch: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118`

---

## 📎 About `Tomato-Leaf-Disease-63/yolov8n.pt`

- This is just a **copy of the base pre-trained YOLOv8n model** (NOT your trained model).
- It is **NOT needed** — your actual pre-trained base model is at `Project/yolov8n.pt`.
- Your **trained model** (with tomato disease detection) is at: `runs/detect/tomato_disease_notebook4/weights/best.pt`
- You can safely ignore or delete `Tomato-Leaf-Disease-63/yolov8n.pt`.

---

## 🔍 How to Use the Trained Model Later

```python
from ultralytics import YOLO

# Load trained model (use the latest successful run)
from pathlib import Path

# Load trained model (use the latest successful run)
run_dir = Path('runs/detect')
matching = sorted(run_dir.glob('tomato_disease_notebook*'), key=lambda p: p.stat().st_mtime)
latest_run = matching[-1] if matching else run_dir / 'tomato_disease_notebook'
model = YOLO(str(latest_run / 'weights' / 'best.pt'))

# Run inference on a new image
results = model.predict(source='your_image.jpg', conf=0.5)

# Show results
results[0].show()
```

Or use the notebook: **`project2_fixed.ipynb`** (just run all cells — no training needed, it will load the existing trained model)

---

## 📌 Quick Reference

| Action | Command / File |
|---|---|
| **Train the model** | `python train_yolov8.py` |
| **Run inference (notebook)** | Open `project2_fixed.ipynb` and run all cells |
| **Check results exist** | Look in `runs/detect/tomato_disease_notebook4/` |
| **Best weights location** | `runs/detect/tomato_disease_notebook4/weights/best.pt` |

---

## 📜 Change History

| Date | What Changed |
|---|---|
| March 2, 2026 | Initial training completed (50 epochs, 3.705 hours, `tomato_disease_notebook4`) |
| March 3, 2026 | Fixed `project2_fixed.ipynb` — changed relative paths to absolute paths so results/weights are always found regardless of notebook working directory |

---

*Last updated: March 3, 2026*

