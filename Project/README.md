# 🍅 YOLOv8 Tomato Leaf Disease Detection

**Status**: ✅ Ready to Train  
**Model**: YOLOv8n (Nano - Fast & Lightweight)  
**Dataset**: [Tomato Leaf Disease Detection (Kaggle)](https://www.kaggle.com/datasets/kpoviesistphane/tomato-leaf-disease-detection) — 1000+ labeled images (9 disease classes)  
**Framework**: PyTorch + Ultralytics YOLO

---

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/revanthkumarreddy-35/Tomato-leaf-disease-detection.git
cd Tomato-leaf-disease-detection/Project
python setup.py          # checks environment & dependencies
pip install -r requirements.txt
```

### 2. Download Dataset
Download from [Kaggle](https://www.kaggle.com/datasets/kpoviesistphane/tomato-leaf-disease-detection) and extract into the `Project/` folder so the structure is:
```
Project/Tomato-Leaf-Disease-63/
├── train/images/
├── valid/images/
└── test/images/
```

### 3. Train the Model
```bash
python train_yolov8.py
```
Or use the Jupyter notebook:
```bash
jupyter notebook train_model.ipynb
```

### 4. Run Inference
```bash
jupyter notebook project2_fixed.ipynb
```

---

## ⚠️ What Was Wrong (The Issue)

Your `project2_fixed.ipynb` showed no output because:

```python
# Your original code did this:
if os.path.exists(best_weights):  # ❌ This file doesn't exist
    # ... code runs but nothing prints
    
# If the file doesn't exist, the entire block is skipped
# Result: NO OUTPUT, no error message
```

**Solution**: Train the model first to create the weights file! ✅

---

## 📊 What Gets Created

After training completes, you'll have:

```
runs/detect/tomato_disease_notebook/
├── weights/
│   ├── best.pt          ← Your trained model (use this!)
│   └── last.pt          ← Last checkpoint
├── results.png          ← Training metrics plot
├── confusion_matrix.png ← Accuracy visualization
├── results.csv          ← Detailed metrics table
└── args.yaml            ← Training configuration
```

---

## 📈 Expected Results

### Training Time
| GPU Type | Time | Quality |
|----------|------|---------|
| RTX 4090 | 10-15 min | ⭐⭐⭐⭐⭐ Excellent |
| RTX 4080 | 15-20 min | ⭐⭐⭐⭐⭐ Excellent |
| RTX 3060 | 45-60 min | ⭐⭐⭐⭐ Good |
| CPU Only | 8-12 hrs | ⭐⭐⭐ OK |

### Performance Metrics
- **mAP@50**: Target >75% (higher is better)
- **Precision**: Target >75% (fewer false positives)
- **Recall**: Target >75% (fewer missed detections)
- **Loss**: Will decrease as training progresses

---

## 🎯 What You Can Do After Training

### 1. View Metrics
```bash
# Opens automatically after training
# Shows graphs of accuracy, loss, etc.
```

### 2. Run Inference on Images
```python
from ultralytics import YOLO

model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')
results = model.predict(source='tomato_image.jpg', conf=0.5)
```

### 3. Run Inference on Webcam
```python
model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')
results = model.predict(source=0, conf=0.5)  # 0 = webcam
```

### 4. Use Jupyter Notebook
Open `project2_fixed.ipynb` and run all cells - it will automatically use your trained model.

---

## 📁 File Structure

```
Project/
├── 🐍 train_yolov8.py ................. Python training script
├── 🔧 setup.py ........................ Cross-platform setup checker
├── 📋 requirements.txt ................ Python dependencies
├── 📓 train_model.ipynb ............... Jupyter notebook version
├── 📓 project2_fixed.ipynb ............ Inference notebook
│
├── 📚 README.md ....................... This file
├── 📚 TRAINING_GUIDE.md ............... Detailed documentation
├── 📚 QUICK_REFERENCE.md .............. Quick commands
│
├── 📦 Tomato-Leaf-Disease-63/ ......... Training dataset (download separately)
│   ├── train/images/
│   ├── valid/images/
│   └── test/images/
│
└── 📊 runs/ ........................... Created after training
    └── detect/tomato_disease_notebook/
        ├── weights/best.pt ............ Your trained model! ⭐
        ├── results.png ................ Metrics graphs
        └── confusion_matrix.png ....... Performance analysis
```

---

## 🔧 System Requirements

### Supported Operating Systems
- **Windows** 10 / 11
- **Linux** (Ubuntu 20.04+, Debian, Fedora, etc.)
- **macOS** 12+ (Intel & Apple Silicon)

### Minimum
- Python 3.8+
- 8GB RAM
- 10GB free disk space

### Recommended for Fast Training
- NVIDIA GPU (RTX 2060 or better) — Windows/Linux
- Apple M1/M2/M3 (MPS acceleration) — macOS
- 16GB+ System RAM
- SSD for faster I/O

### Without GPU
- Any modern multi-core CPU
- 16GB RAM
- Takes 8-12 hours to train

---

## 💻 Installation

### Step 1: Install Dependencies
```bash
cd Project
pip install -r requirements.txt
```

#### GPU-specific installs (optional, for faster training):

**Windows / Linux (NVIDIA GPU):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

**macOS (Apple Silicon — MPS acceleration works automatically):**
```bash
pip install torch torchvision torchaudio
```

**CPU only (any OS):**
```bash
pip install torch torchvision torchaudio
```

### Step 2: Verify Installation
```bash
python setup.py
```
Or manually:
```bash
python -c "import torch; print(f'GPU: {torch.cuda.is_available()}')"
python -c "from ultralytics import YOLO; print('YOLOv8 OK')"
```

---

## 🎬 Step-by-Step Training

### Step 1: Start Training
```bash
python train_yolov8.py
```

You'll see:
```
✅ GPU Available: NVIDIA GeForce RTX 4090
📂 Dataset location: ./Tomato-Leaf-Disease-63
   ✅ Train images: 1234
   ✅ Validation images: 256
   ✅ Test images: 128

🤖 Loading YOLOv8n pre-trained model...
✅ Model loaded

======================================================================
🚀 STARTING TRAINING
======================================================================

Epoch 1/50:   20% |████░░░░░░| Loss: 2.34
Epoch 2/50:   40% |████████░░| Loss: 1.89
...
```

### Step 2: Wait for Completion
- GPU users: 30-60 minutes
- CPU users: 8-12 hours
- You can see progress in real-time

### Step 3: View Results
Automatic plots will display:
- Training loss graph
- Validation metrics
- Sample detections

### Step 4: Run Inference
```bash
jupyter notebook project2_fixed.ipynb
# Click "Run All" - it will show detection results!
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| **"CUDA out of memory"** | Reduce batch size: `batch=8` in train_yolov8.py |
| **"GPU not found"** | Update NVIDIA drivers, reinstall PyTorch with CUDA |
| **"Dataset not found"** | Make sure `Tomato-Leaf-Disease-63/` folder is in the `Project/` directory |
| **"Very slow training"** | You're using CPU. Install GPU drivers or use Google Colab |
| **"No module ultralytics"** | Run: `pip install ultralytics --upgrade` |
| **Training crashed** | Reduce batch size or epoch count |

---

## 📊 Disease Classes Detected

Your model will detect these 9 tomato diseases:

1. **Early Blight** - Brown spots with concentric rings
2. **Healthy** - No disease present
3. **Late Blight** - Water-soaked spots
4. **Leaf Miner** - Winding tunnels in leaves
5. **Leaf Mold** - Velvety fungal growth
6. **Mosaic Virus** - Mottled, discolored patches
7. **Septoria Leaf Spot** - Small circular spots with dark borders
8. **Spider Mites** - Fine webbing, stippled leaves
9. **Yellow Leaf Curl Virus** - Yellowing and curling of leaves

---

## 🔄 Model Architecture

```
Image Input (640×640)
        ↓
YOLOv8n Backbone
  - 3 detection heads
  - ~3.2M parameters
  - Real-time speed
        ↓
9 Class Output + Bounding Boxes
```

Benefits of YOLOv8n (Nano):
- ⚡ Fast inference (suitable for mobile/edge)
- 💾 Small file size (~6MB)
- 🎯 Good accuracy for most use cases
- 📱 Can run on CPU if needed

---

## 📚 Advanced Usage

### Use Larger Model for Better Accuracy
```python
from ultralytics import YOLO

# In train_yolov8.py, change:
# model = YOLO('yolov8n.pt')  # nano (current)
# to:
model = YOLO('yolov8m.pt')  # medium (better)
# or:
model = YOLO('yolov8l.pt')  # large (best but slower)
```

### Train for More Epochs
```python
# In train_yolov8.py, change:
results = model.train(
    epochs=100,  # Instead of 50
    # ... rest of config
)
```

### Fine-tune on Custom Data
```python
# After training, continue training on new data:
model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')
results = model.train(
    data='new_data.yaml',
    epochs=50,
    device=0
)
```

---

## 🌐 Export for Deployment

After training, export your model:

```python
from ultralytics import YOLO

model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')

# Export to different formats:
model.export(format='onnx')   # For C#/.NET
model.export(format='tflite') # For mobile
model.export(format='torchscript')  # PyTorch
```

---

## 📞 Support & Resources

### Documentation Files
- `TRAINING_GUIDE.md` - Comprehensive guide
- `SOLUTION_SUMMARY.md` - What was fixed
- `QUICK_REFERENCE.md` - Quick commands

### Online Resources
- **YOLOv8 Official**: https://docs.ultralytics.com/
- **GitHub**: https://github.com/ultralytics/ultralytics
- **Community Forum**: https://github.com/ultralytics/ultralytics/issues

### Common Questions

**Q: Do I need GPU?**  
A: No, but training will be 10-100x slower on CPU.

**Q: How much disk space?**  
A: ~10GB total (dataset + trained models).

**Q: Can I use with Raspberry Pi?**  
A: Yes, after training, the model can run on Pi with CPU inference.

**Q: How do I improve accuracy?**  
A: Train longer (100+ epochs), use larger model (yolov8m/l), collect more data.

---

## ✅ Verification Checklist

Before running training, verify:

- [ ] Python 3.8+ installed: `python --version`
- [ ] In the `Project/` directory
- [ ] Dataset exists: `Tomato-Leaf-Disease-63/` folder present
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Run `python setup.py` — all checks pass
- [ ] GPU available (optional): `nvidia-smi` (NVIDIA) or check via `python setup.py`

---

## 🎯 Next Steps

1. **Run Training**
   ```bash
   python train_yolov8.py
   ```

2. **Wait for Completion** (30-60 minutes)

3. **Check Results**
   - View metrics: `runs/detect/tomato_disease_notebook/results.png`
   - View model: `runs/detect/tomato_disease_notebook/weights/best.pt`

4. **Run Inference**
   ```bash
   jupyter notebook project2_fixed.ipynb
   ```

5. **See Detections** - The notebook will automatically show:
   - Training metrics plot
   - Sample detections with bounding boxes
   - Confidence scores per class

---

## 🎉 Summary

| Step | Command | Time |
|------|---------|------|
| Install | `pip install torch ultralytics` | 2 min |
| Train | `python train_yolov8.py` | 30-60 min |
| Test | `jupyter notebook project2_fixed.ipynb` | 1 min |

**Total Time**: ~1-2 hours (mostly waiting for training)

---

## 📝 License & Attribution

- YOLOv8: MIT License (Ultralytics)
- Dataset: Provided in your project
- Training scripts: Created for your project

---

**Ready to start? Run this command:**

```bash
python train_yolov8.py
```

**Good luck! 🚀🍅**

---

*Last Updated: March 2026*  
*Status: Production Ready ✅*  
*Version: 1.0*

