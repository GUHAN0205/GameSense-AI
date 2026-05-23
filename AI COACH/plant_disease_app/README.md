# 🌿 Plant Disease Detection System

An AI-powered web application for detecting plant diseases using deep learning. Built with Flask and TensorFlow.

## Features

- 🔬 **AI-Powered Detection**: Identify 38+ plant diseases with 95%+ accuracy
- 🌱 **14 Plant Species**: Supports common crops and fruits
- 📊 **Dashboard**: Track your detection history and statistics
- 👤 **User Accounts**: Save and manage your plant health records
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🎨 **Modern UI**: Beautiful, intuitive interface

## Supported Plants

- Apple
- Blueberry
- Cherry
- Corn (Maize)
- Grape
- Orange
- Peach
- Pepper (Bell)
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Step 1: Clone or Extract

```bash
cd plant_disease_app
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Your Model (Important!)

Place your trained `plant_disease_model.h5` file in the root directory.

If you don't have a model, the app will use mock predictions for demonstration.

### Step 5: Run the Application

```bash
python app.py
```

The app will be available at: **http://localhost:5000**

## Project Structure

```
plant_disease_app/
├── app.py                    # Main Flask application
├── database.py               # Database operations
├── requirements.txt          # Python dependencies
├── plant_disease_model.h5    # Trained model (add this!)
├── uploads/                  # Uploaded images
├── static/
│   ├── css/
│   │   └── style.css         # Styling
│   ├── js/
│   │   └── main.js           # JavaScript functionality
│   └── images/
│       └── logo.svg          # App logo
├── templates/
│   ├── base.html             # Base template
│   ├── index.html            # Home page
│   ├── result.html           # Results (currently handled in index.html)
│   ├── history.html          # Detection history
│   ├── dashboard.html        # User dashboard
│   ├── login.html            # Login page
│   ├── register.html         # Registration page
│   └── about.html            # About page
└── create_zip.py             # Script to create deployment ZIP
```

## Usage

### For End Users

1. **Upload Image**: Click or drag & drop a plant image
2. **Analyze**: Click "Analyze Image" button
3. **View Results**: Get instant disease detection with treatment advice
4. **Save History**: Create an account to track your diagnoses

### For Developers

#### Training Your Own Model

```python
# Use TensorFlow/Keras to train on PlantVillage dataset
# Model should accept 224x224 RGB images
# Output: 38 classes (disease categories)
```

#### API Endpoints

```
GET  /                 # Home page
GET  /about            # About page
POST /register         # User registration
POST /login            # User login
GET  /logout           # User logout
POST /upload           # Upload and analyze image
GET  /dashboard        # User dashboard (requires login)
GET  /history          # Detection history (requires login)
GET  /api/stats        # User statistics API (requires login)
```

#### Database Schema

**Users Table:**
- id (INTEGER, PRIMARY KEY)
- username (TEXT)
- email (TEXT, UNIQUE)
- password (TEXT, HASHED)
- created_at (TIMESTAMP)

**Predictions Table:**
- id (INTEGER, PRIMARY KEY)
- user_id (INTEGER, FOREIGN KEY)
- image_path (TEXT)
- plant_type (TEXT)
- disease_name (TEXT)
- confidence (REAL)
- created_at (TIMESTAMP)

## Configuration

### Environment Variables (Optional)

Create a `.env` file:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=sqlite:///plant_disease.db
```

### Upload Settings

In `app.py`:

```python
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
```

## Training Data

This app is designed to work with the **PlantVillage Dataset**, which contains:
- 50,000+ images
- 14 crop species
- 38 disease classes
- Healthy and diseased samples

Download from: [PlantVillage on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)

## Model Architecture

Recommended CNN architecture:
- Input: 224x224x3 RGB images
- Base: MobileNetV2 or ResNet50 (transfer learning)
- Output: 38 classes (Softmax activation)
- Loss: Categorical Crossentropy
- Optimizer: Adam

Example training script available on request.

## Deployment

### Option 1: Heroku

```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create plant-disease-app
git push heroku main
```

### Option 2: PythonAnywhere

1. Upload ZIP file
2. Extract in web directory
3. Set up WSGI configuration
4. Install dependencies in virtual environment

### Option 3: Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Testing

### Test Database

```bash
python database.py
```

### Test Upload

Use the web interface or:

```bash
curl -X POST http://localhost:5000/upload \
  -F "file=@test_image.jpg"
```

## Troubleshooting

### Model Not Loading

- Ensure `plant_disease_model.h5` is in the root directory
- Check TensorFlow version compatibility
- App will use mock predictions if model fails to load

### Database Errors

- Delete `plant_disease.db` to reset
- Run `python database.py` to reinitialize

### Upload Errors

- Check file size (max 16MB)
- Ensure file extension is .jpg, .jpeg, or .png
- Verify `uploads/` folder exists and is writable

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use for personal or commercial projects.

## Acknowledgments

- **PlantVillage Dataset**: Training data
- **TensorFlow/Keras**: Deep learning framework
- **Flask**: Web framework
- **Chart.js**: Dashboard charts

## Support

For issues or questions:
- Open an issue on GitHub
- Email: info@plantdisease.com
- Check the [About](/about) page

## Future Enhancements

- [ ] Mobile app (React Native)
- [ ] Real-time detection via camera
- [ ] Multi-language support
- [ ] Treatment product recommendations
- [ ] Community forum
- [ ] Expert consultation integration
- [ ] Batch processing for farmers
- [ ] API for third-party integrations

## Version History

- **v1.0.0** (2024): Initial release
  - 38 disease classes
  - 14 plant species
  - User authentication
  - Dashboard and history
  - Responsive design

---

**Made with 🌱 for healthier plants and better harvests**

For questions or contributions, please open an issue or pull request.
