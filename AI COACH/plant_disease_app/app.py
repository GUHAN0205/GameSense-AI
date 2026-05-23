"""
Plant Disease Detection Application
A Flask-based web app for detecting plant diseases using deep learning
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from database import Database
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Initialize database
db = Database()

# Disease classes (38 classes from PlantVillage dataset)
DISEASE_CLASSES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# Load model
try:
    model = tf.keras.models.load_model('plant_disease_model.h5')
    print("✓ Model loaded successfully")
except Exception as e:
    print(f"⚠ Warning: Could not load model - {e}")
    print("  Using mock predictions for demonstration")
    model = None

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static/images', exist_ok=True)


# Helper functions
def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def login_required(f):
    """Decorator to require login for certain routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def preprocess_image(image_path):
    """Preprocess image for model prediction"""
    try:
        img = Image.open(image_path)
        img = img.resize((224, 224))  # Resize to model input size
        img_array = np.array(img)
        
        # Normalize
        img_array = img_array / 255.0
        
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None


def predict_disease(image_path):
    """Predict plant disease from image"""
    try:
        # Preprocess image
        img_array = preprocess_image(image_path)
        if img_array is None:
            return None, 0.0
        
        # Make prediction
        if model is not None:
            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class_index])
            predicted_class = DISEASE_CLASSES[predicted_class_index]
        else:
            # Mock prediction for demonstration
            import random
            predicted_class_index = random.randint(0, len(DISEASE_CLASSES) - 1)
            predicted_class = DISEASE_CLASSES[predicted_class_index]
            confidence = random.uniform(0.75, 0.99)
        
        return predicted_class, confidence
    
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, 0.0


def get_disease_info(disease_name):
    """Get information about the disease"""
    # Parse disease name
    parts = disease_name.split('___')
    plant = parts[0].replace('_', ' ')
    disease = parts[1].replace('_', ' ') if len(parts) > 1 else 'Unknown'
    
    # Disease information database
    disease_info = {
        'healthy': {
            'description': 'Your plant appears to be healthy! No disease detected.',
            'treatment': 'Continue with regular care and maintenance.',
            'prevention': 'Maintain good watering practices, ensure proper sunlight, and monitor regularly.'
        },
        'Apple scab': {
            'description': 'A fungal disease causing dark, scabby lesions on leaves and fruit.',
            'treatment': 'Apply fungicides, remove infected leaves, improve air circulation.',
            'prevention': 'Plant resistant varieties, avoid overhead watering, remove fallen leaves.'
        },
        'Black rot': {
            'description': 'Fungal disease causing black, rotted areas on fruit and leaves.',
            'treatment': 'Prune infected areas, apply copper-based fungicides.',
            'prevention': 'Ensure good drainage, avoid wetting leaves, sanitize pruning tools.'
        },
        'Powdery mildew': {
            'description': 'White, powdery fungal growth on leaves and stems.',
            'treatment': 'Apply sulfur or neem oil sprays, increase air circulation.',
            'prevention': 'Avoid overhead watering, ensure proper spacing, choose resistant varieties.'
        },
        'Bacterial spot': {
            'description': 'Bacterial infection causing dark spots with yellow halos.',
            'treatment': 'Apply copper-based bactericides, remove infected plants.',
            'prevention': 'Use disease-free seeds, avoid overhead watering, rotate crops.'
        },
        'Early blight': {
            'description': 'Fungal disease with concentric ring patterns on leaves.',
            'treatment': 'Apply fungicides, remove infected leaves, mulch around plants.',
            'prevention': 'Rotate crops, water at base, use resistant varieties.'
        },
        'Late blight': {
            'description': 'Destructive disease causing water-soaked lesions and white mold.',
            'treatment': 'Apply fungicides immediately, destroy infected plants.',
            'prevention': 'Use resistant varieties, ensure good drainage, avoid overhead watering.'
        }
    }
    
    # Match disease to info
    for key in disease_info:
        if key.lower() in disease.lower():
            return {
                'plant': plant,
                'disease': disease,
                **disease_info[key]
            }
    
    # Default info
    return {
        'plant': plant,
        'disease': disease,
        'description': f'{disease} detected on {plant}.',
        'treatment': 'Consult with a plant pathologist for specific treatment.',
        'prevention': 'Maintain good plant hygiene and monitor regularly.'
    }


# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))
        
        # Check if user exists
        if db.get_user_by_email(email):
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))
        
        # Hash password and create user
        hashed_password = generate_password_hash(password)
        user_id = db.create_user(username, email, hashed_password)
        
        if user_id:
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. Please try again.', 'danger')
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = db.get_user_by_email(email)
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f'Welcome back, {user["username"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload():
    """Handle image upload and prediction"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Use PNG, JPG, or JPEG'}), 400
    
    try:
        # Save file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Predict disease
        disease, confidence = predict_disease(filepath)
        
        if disease is None:
            return jsonify({'error': 'Prediction failed'}), 500
        
        # Get disease information
        disease_info = get_disease_info(disease)
        
        # Save to database if user is logged in
        if 'user_id' in session:
            db.save_prediction(
                session['user_id'],
                filename,
                disease_info['plant'],
                disease_info['disease'],
                confidence
            )
        
        # Return results
        return jsonify({
            'success': True,
            'filename': filename,
            'plant': disease_info['plant'],
            'disease': disease_info['disease'],
            'confidence': round(confidence * 100, 2),
            'description': disease_info['description'],
            'treatment': disease_info['treatment'],
            'prevention': disease_info['prevention']
        })
    
    except Exception as e:
        print(f"Error during upload: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/result')
def result():
    """Display prediction results"""
    return render_template('result.html')


@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    stats = db.get_user_stats(session['user_id'])
    recent_predictions = db.get_user_predictions(session['user_id'], limit=5)
    
    return render_template('dashboard.html', 
                         stats=stats, 
                         recent_predictions=recent_predictions)


@app.route('/history')
@login_required
def history():
    """Prediction history"""
    predictions = db.get_user_predictions(session['user_id'])
    return render_template('history.html', predictions=predictions)


@app.route('/api/stats')
@login_required
def api_stats():
    """API endpoint for dashboard statistics"""
    stats = db.get_user_stats(session['user_id'])
    return jsonify(stats)


# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('index.html'), 500


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🌿 Plant Disease Detection App")
    print("="*50)
    print("\nStarting server...")
    print("Access the app at: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
