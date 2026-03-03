# Tomato Leaf Disease Detection - YOLOv8 Training Guide

## Overview
This project uses YOLOv8 (a state-of-the-art object detection model) to detect and classify 9 different tomato leaf diseases:
1. Early Blight
2. Healthy (no disease)
3. Late Blight
4. Leaf Miner
5. Leaf Mold
6. Mosaic Virus
7. Septoria Leaf Spot
8. Spider Mites
9. Yellow Leaf Curl Virus

## Files in This Project

### Training Scripts
- **`train_yolov8.py`** - Standalone Python script for training (recommended for most users)
- **`train_model.ipynb`** - Jupyter notebook for training with step-by-step visualization

### Inference/Testing Scripts
- **`project2_fixed.ipynb`** - Jupyter notebook to run inference on trained model

### Dataset Location
- **`./Tomato-Leaf-Disease-63/`** - Your training dataset
  - `train/images/` - Training images (~1000s of images)
  - `valid/images/` - Validation images
  - `test/images/` - Test images

## System Requirements

### Recommended
- **GPU**: NVIDIA GPU with CUDA support (RTX 3060 or better) - cuts training time from hours to 30-60 minutes
- **VRAM**: 4GB+ (8GB recommended for batch size 16)
- **Storage**: 10GB+ free space (for model and training data)

### Minimum
- **CPU**: Multi-core processor (will train slowly)
- **RAM**: 8GB+
- **Storage**: 10GB+ free space

## Installation

### Step 1: Install Dependencies
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install ultralytics matplotlib
```

For CPU-only (if you don't have GPU):
```bash
pip install torch torchvision torchaudio
pip install ultralytics matplotlib
```

### Step 2: Navigate to Project Directory
```bash
cd C:\Users\revan\PyCharmMiscProject\Project
```

## Training Instructions

### Option A: Using Python Script (Recommended)
```bash
python train_yolov8.py
```

**Advantages:**
- Simplest to run
- Clear progress output
- Automatic error handling

### Option B: Using Jupyter Notebook
```bash
jupyter notebook train_model.ipynb
```

Then run each cell in sequence.

---

## Training Process Explained

### What Happens During Training:
1. **Data Loading** - Loads all training images and labels
2. **Model Initialization** - Loads YOLOv8n pre-trained weights
3. **Epochs** - Iterates through dataset 50 times
4. **Loss Calculation** - Measures how well model detects objects
5. **Backpropagation** - Updates weights to improve accuracy
6. **Validation** - Tests on validation set each epoch
7. **Checkpointing** - Saves best model weights
8. **Results** - Generates metrics and plots

### Expected Training Time:
| Device | Time |
|--------|------|
| RTX 3060/3070 (12GB VRAM) | 30-45 minutes |
| RTX 4080 (24GB VRAM) | 15-20 minutes |
| RTX 4090 (24GB VRAM) | 10-15 minutes |
| CPU (i7/Ryzen 5) | 8-12 hours |

## Output Files

After training completes, you'll find:

```
runs/detect/tomato_disease_notebook/
├── weights/
│   ├── best.pt          ← Best model (use this!)
│   └── last.pt          ← Last checkpoint
├── results.png          ← Training metrics plot
├── confusion_matrix.png ← Confusion matrix
└── results.csv          ← Detailed metrics
```

## Using the Trained Model

### For Inference (Testing):

#### In Jupyter Notebook:
```python
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load trained model
model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')

# Run inference
results = model.predict(source='path/to/tomato_image.jpg', conf=0.5)

# Display results
for r in results:
    im_array = r.plot()
    plt.imshow(im_array[..., ::-1])
    plt.show()
```

#### Using project2_fixed.ipynb:
The fixed notebook automatically uses the trained model if weights exist.

### For Real-Time Detections:
```python
from ultralytics import YOLO

model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')

# On webcam
results = model.predict(source=0, conf=0.5)  # 0 = webcam

# On video file
results = model.predict(source='video.mp4', conf=0.5)
```

## Troubleshooting

### Issue: "CUDA out of memory"
**Solution:** Reduce batch size in `train_yolov8.py`:
```python
# Change this line:
batch=16,  # Reduce to 8 or 4
```

### Issue: Very slow training (using CPU)
**Solution:** Install GPU drivers
- Update NVIDIA drivers to latest version
- Reinstall PyTorch with GPU support

### Issue: "No module named 'ultralytics'"
**Solution:**
```bash
pip install ultralytics --upgrade
```

### Issue: Dataset not found
**Make sure you're running the script from the correct directory:**
```bash
# Correct:
cd C:\Users\revan\PyCharmMiscProject\Project
python train_yolov8.py

# Or update dataset path in script
```

## Performance Metrics

The training will output:
- **mAP@50** - Mean Average Precision at IoU=0.5 (higher is better, target: >0.6)
- **mAP@50-95** - Mean AP across IoU thresholds (target: >0.4)
- **Precision** - Of positives predicted as positive (target: >0.7)
- **Recall** - Of actual positives found (target: >0.7)
- **Loss** - Training error (should decrease over epochs)

## Tips for Better Results

1. **More Epochs**: If accuracy is still low, train for 100 epochs instead of 50
2. **Larger Model**: Use `yolov8m.pt` (medium) instead of `yolov8n.pt` (nano) for better accuracy
3. **Better Hardware**: GPU training is 10-100x faster than CPU
4. **Data Augmentation**: YOLOv8 automatically applies augmentations
5. **Longer Training**: Run validation after training completes to check real-world performance

## Next Steps

1. **Train the model** using one of the scripts above
2. **Check results** in `runs/detect/tomato_disease_notebook/`
3. **Test inference** using `project2_fixed.ipynb`
4. **Deploy** the model in your application

---

## Additional Resources

- **YOLOv8 Docs**: https://docs.ultralytics.com/
- **Ultralytics GitHub**: https://github.com/ultralytics/ultralytics
- **Dataset Format**: YOLOv8 expects COCO-style annotations (already in your dataset)

---

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify dataset exists at `./Tomato-Leaf-Disease-63/`
3. Ensure all dependencies are installed: `pip list | grep -E "torch|ultralytics"`
4. Check available GPU memory: `nvidia-smi` (if NVIDIA GPU)

---

**Happy Training! 🚀**

