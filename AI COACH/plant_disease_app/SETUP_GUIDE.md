# 🚀 Complete Setup Guide

Step-by-step instructions to get the Plant Disease Detection app running.

## Quick Start (5 Minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open browser
# Go to: http://localhost:5000
```

**That's it!** The app will work with mock predictions.

---

## Detailed Setup

### 1. System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended with TensorFlow)
- **Disk Space**: 500MB minimum
- **OS**: Windows, macOS, or Linux

### 2. Verify Python Installation

```bash
python --version
# Should show: Python 3.8.x or higher

pip --version
# Should be installed with Python
```

### 3. Download/Extract Project

```bash
# If you have a ZIP file:
unzip plant_disease_app.zip
cd plant_disease_app

# If cloning from Git:
git clone <repository-url>
cd plant_disease_app
```

### 4. Create Virtual Environment (Recommended)

**Why?** Keeps dependencies isolated from your system Python.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask (web framework)
- TensorFlow (AI model)
- Pillow (image processing)
- NumPy (numerical operations)
- Werkzeug (security utilities)

**Estimated time:** 2-5 minutes depending on internet speed.

### 6. Optional: Add Your Model

If you have a trained model:

1. Rename it to `plant_disease_model.h5`
2. Place it in the root directory (same folder as `app.py`)

**Don't have a model?** No problem! The app will use mock predictions for testing.

### 7. Initialize Database

The database is automatically created when you first run the app.

To manually test:
```bash
python database.py
```

You should see: `✓ Database initialized`

### 8. Run the Application

```bash
python app.py
```

**Expected output:**
```
==================================================
🌿 Plant Disease Detection App
==================================================

Starting server...
Access the app at: http://localhost:5000

Press Ctrl+C to stop the server
```

### 9. Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

You should see the home page with the upload interface!

---

## First Time Usage

### Create an Account

1. Click **Register** in the navigation
2. Fill in:
   - Username
   - Email
   - Password (min 6 characters)
3. Click **Create Account**
4. You'll be redirected to login

### Login

1. Enter your email and password
2. Click **Login**
3. You'll see your dashboard

### Upload Your First Image

1. Go to the home page
2. Click or drag an image of a plant leaf
3. Click **Analyze Image**
4. Wait a few seconds
5. View your results!

---

## Configuration

### Change Port

In `app.py`, modify the last line:

```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Changed to 8000
```

### Upload Folder

In `app.py`:

```python
app.config['UPLOAD_FOLDER'] = 'my_uploads'  # Custom folder
```

Create the folder:
```bash
mkdir my_uploads
```

### Max File Size

In `app.py`:

```python
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB
```

### Secret Key (Important for Production!)

In `app.py`:

```python
app.config['SECRET_KEY'] = 'your-unique-secret-key-here-change-this'
```

Generate a secure key:
```python
import secrets
print(secrets.token_hex(32))
```

---

## Training Your Own Model

### 1. Get the Dataset

Download PlantVillage from Kaggle:
https://www.kaggle.com/datasets/emmarex/plantdisease

### 2. Basic Training Script

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    'path/to/dataset',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    'path/to/dataset',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Model
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(38, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)

# Save
model.save('plant_disease_model.h5')
```

### 3. Test Your Model

```python
from PIL import Image
import numpy as np

# Load model
model = tf.keras.models.load_model('plant_disease_model.h5')

# Prepare image
img = Image.open('test_image.jpg').resize((224, 224))
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions[0])
confidence = predictions[0][predicted_class]

print(f"Predicted class: {predicted_class}")
print(f"Confidence: {confidence:.2%}")
```

---

## Deployment

### Local Network Access

To access from other devices on your network:

1. Find your local IP:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Run with host='0.0.0.0':
   ```bash
   python app.py
   ```

3. Access from other devices:
   ```
   http://YOUR_LOCAL_IP:5000
   ```

### Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for:
- Heroku
- PythonAnywhere
- AWS
- DigitalOcean
- Docker

---

## Troubleshooting

### Problem: "Module not found" errors

**Solution:**
```bash
# Make sure virtual environment is activated
# Then reinstall:
pip install -r requirements.txt
```

### Problem: TensorFlow installation fails

**Solution:**
```bash
# Use CPU-only version:
pip uninstall tensorflow
pip install tensorflow-cpu==2.13.0
```

### Problem: "Port 5000 already in use"

**Solution:**
```bash
# Use different port
# In app.py, change:
app.run(debug=True, port=8000)
```

### Problem: Upload fails

**Solution:**
- Check `uploads/` folder exists
- Verify folder permissions (must be writable)
- Check file size < 16MB
- Ensure file extension is .jpg, .jpeg, or .png

### Problem: Database errors

**Solution:**
```bash
# Reset database
rm plant_disease.db
python database.py
```

### Problem: Model not loading

**Solution:**
- Verify model file exists: `plant_disease_model.h5`
- Check TensorFlow version: `pip show tensorflow`
- App will use mock predictions if model fails

---

## FAQ

**Q: Do I need a GPU?**  
A: No, CPU is fine. GPU speeds up training but not necessary for prediction.

**Q: Can I use my own dataset?**  
A: Yes! Just retrain the model with your images.

**Q: Is there a mobile app?**  
A: Not yet, but the web app is mobile-responsive.

**Q: Can I add more plant species?**  
A: Yes! Train a new model with additional classes.

**Q: How accurate is the detection?**  
A: With a properly trained model, 95%+ accuracy is achievable.

**Q: Can I use this commercially?**  
A: Yes, it's MIT licensed. Use freely!

---

## Getting Help

1. **Check README.md** - General information
2. **Check this guide** - Setup and configuration
3. **Check TROUBLESHOOTING.md** - Common issues
4. **GitHub Issues** - Report bugs or ask questions
5. **Email** - info@plantdisease.com

---

## Next Steps

After getting the app running:

1. ✅ Create an account
2. ✅ Upload test images
3. ✅ Explore the dashboard
4. ✅ Check your history
5. ⬜ Train your own model
6. ⬜ Deploy to production
7. ⬜ Share with others!

---

**Congratulations!** 🎉

You now have a fully functional plant disease detection system!

Start protecting your plants with AI! 🌱
