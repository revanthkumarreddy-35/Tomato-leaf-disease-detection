"""
YOLOv8 Tomato Leaf Disease Detection - Training Script
This script trains a YOLOv8n model to detect 9 different tomato leaf diseases.
"""

import torch
from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    # Check GPU availability
    device = 0 if torch.cuda.is_available() else 'cpu'
    if device == 0:
        print(f"✅ GPU Available: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠️ GPU not available, using CPU (training will be slow)")

    # Dataset configuration
    dataset_path = "./Tomato-Leaf-Disease-63"
    print(f"\n📂 Dataset location: {dataset_path}")

    # Verify dataset exists
    if not os.path.exists(dataset_path):
        print("❌ ERROR: Dataset not found!")
        return

    # Check dataset structure
    train_images = f"{dataset_path}/train/images"
    val_images = f"{dataset_path}/valid/images"
    test_images = f"{dataset_path}/test/images"

    if os.path.exists(train_images):
        train_count = len(os.listdir(train_images))
        print(f"   ✅ Train images: {train_count}")
    else:
        print(f"   ❌ Train images not found")
        return

    if os.path.exists(val_images):
        val_count = len(os.listdir(val_images))
        print(f"   ✅ Validation images: {val_count}")

    if os.path.exists(test_images):
        test_count = len(os.listdir(test_images))
        print(f"   ✅ Test images: {test_count}")

    # Create data.yaml
    print("\n📝 Creating data.yaml configuration...")
    data_yaml = f"""path: {os.path.abspath(dataset_path)}
train: train/images
val: valid/images
test: test/images

nc: 9
names: [
  'Early_Blight', 'Healthy', 'Late_Blight', 'Leaf_Miner',
  'Leaf_Mold', 'Mosaic_Virus', 'Septoria_Leaf_Spot',
  'Spider_Mites', 'Yellow_Leaf_Curl_Virus'
]
"""

    with open("data.yaml", "w") as f:
        f.write(data_yaml)
    print("✅ data.yaml created")

    # Load YOLOv8 model
    print("\n🤖 Loading YOLOv8n pre-trained model...")
    model = YOLO('yolov8n.pt')
    print("✅ Model loaded")

    # Train the model
    print("\n" + "="*70)
    print("🚀 STARTING TRAINING (This may take 1-4 hours depending on GPU)")
    print("="*70)

    results = model.train(
        data='data.yaml',
        epochs=50,              # Number of training epochs
        imgsz=640,              # Image size
        batch=16,               # Batch size (adjust based on GPU memory: 8, 16, 32)
        device=device,          # Use GPU if available
        name='tomato_disease_notebook',
        patience=10,            # Early stopping patience
        save=True,              # Save checkpoints
        verbose=True,           # Verbose output
        plots=True,             # Save plots
    )

    print("\n" + "="*70)
    print("✅ TRAINING COMPLETE!")
    print("="*70)

    # Find the actual output directory (YOLO auto-increments: notebook, notebook2, notebook3...)
    run_dir = Path('runs/detect')
    matching = sorted(run_dir.glob('tomato_disease_notebook*'), key=os.path.getmtime)
    latest_run = str(matching[-1]) if matching else 'runs/detect/tomato_disease_notebook'

    results_path = os.path.join(latest_run, 'results.png')
    weights_path = os.path.join(latest_run, 'weights', 'best.pt')

    print(f"\n📊 Results Summary:")
    print(f"   📁 Run directory: {latest_run}")
    print(f"   📈 Metrics plot: {results_path}")
    print(f"   💾 Best weights: {weights_path}")

    if os.path.exists(results_path):
        print(f"\n📊 Displaying training metrics...")
        plt.figure(figsize=(15, 10))
        img = plt.imread(results_path)
        plt.imshow(img)
        plt.axis('off')
        plt.title('Training Metrics')
        plt.tight_layout()
        plt.show()

    # Test on a sample image
    print(f"\n🔍 Testing model on sample images...")
    if os.path.exists(weights_path):
        trained_model = YOLO(weights_path)
        test_img_path = './Tomato-Leaf-Disease-63/test/images'

        if os.path.exists(test_img_path):
            sample_images = [os.path.join(test_img_path, f) for f in os.listdir(test_img_path) if f.endswith(('.jpg', '.png'))]

            if sample_images:
                print(f"Found {len(sample_images)} test images. Testing first 3...")

                for idx, test_image in enumerate(sample_images[:3]):
                    print(f"\n   Test image {idx+1}: {os.path.basename(test_image)}")
                    results = trained_model.predict(source=test_image, conf=0.5, verbose=False)

                    for r in results:
                        print(f"      ✓ Detections: {len(r.boxes)} object(s) found")
                        im_array = r.plot()

                        plt.figure(figsize=(10, 8))
                        plt.imshow(im_array[..., ::-1])
                        plt.axis('off')
                        plt.title(f'Detection - {os.path.basename(test_image)}')
                        plt.tight_layout()
                        plt.show()

    print("\n" + "="*70)
    print("✅ Training pipeline complete!")
    print("="*70)
    print("\n📌 Next steps:")
    print("   1. Use project2_fixed.ipynb to run inference on new images")
    print("   2. Or use: model = YOLO('runs/detect/tomato_disease_notebook/weights/best.pt')")
    print("   3. results = model.predict(source='image.jpg')")

if __name__ == "__main__":
    main()

