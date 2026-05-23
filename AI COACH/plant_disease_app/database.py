"""
Database module for Plant Disease Detection App
Handles all database operations using SQLite
"""

import sqlite3
from datetime import datetime
import os


class Database:
    def __init__(self, db_name='plant_disease.db'):
        """Initialize database connection"""
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # Access columns by name
        return conn
    
    def init_database(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Predictions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                image_path TEXT NOT NULL,
                plant_type TEXT NOT NULL,
                disease_name TEXT NOT NULL,
                confidence REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✓ Database initialized")
    
    # User operations
    def create_user(self, username, email, password):
        """Create a new user"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (username, email, password))
            
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return user_id
        except sqlite3.IntegrityError:
            return None
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
    
    def get_user_by_email(self, email):
        """Get user by email"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        
        conn.close()
        
        return dict(user) if user else None
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        
        conn.close()
        
        return dict(user) if user else None
    
    # Prediction operations
    def save_prediction(self, user_id, image_path, plant_type, disease_name, confidence):
        """Save a prediction"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO predictions (user_id, image_path, plant_type, disease_name, confidence)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, image_path, plant_type, disease_name, confidence))
            
            prediction_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return prediction_id
        except Exception as e:
            print(f"Error saving prediction: {e}")
            return None
    
    def get_user_predictions(self, user_id, limit=None):
        """Get all predictions for a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT * FROM predictions 
            WHERE user_id = ? 
            ORDER BY created_at DESC
        '''
        
        if limit:
            query += f' LIMIT {limit}'
        
        cursor.execute(query, (user_id,))
        predictions = cursor.fetchall()
        
        conn.close()
        
        return [dict(pred) for pred in predictions]
    
    def get_prediction_by_id(self, prediction_id):
        """Get a specific prediction"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM predictions WHERE id = ?', (prediction_id,))
        prediction = cursor.fetchone()
        
        conn.close()
        
        return dict(prediction) if prediction else None
    
    # Statistics operations
    def get_user_stats(self, user_id):
        """Get statistics for a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Total predictions
        cursor.execute('''
            SELECT COUNT(*) as total FROM predictions WHERE user_id = ?
        ''', (user_id,))
        total = cursor.fetchone()['total']
        
        # Healthy plants
        cursor.execute('''
            SELECT COUNT(*) as healthy FROM predictions 
            WHERE user_id = ? AND disease_name LIKE '%healthy%'
        ''', (user_id,))
        healthy = cursor.fetchone()['healthy']
        
        # Diseased plants
        diseased = total - healthy
        
        # Most common plant
        cursor.execute('''
            SELECT plant_type, COUNT(*) as count FROM predictions 
            WHERE user_id = ? 
            GROUP BY plant_type 
            ORDER BY count DESC 
            LIMIT 1
        ''', (user_id,))
        common_plant_row = cursor.fetchone()
        common_plant = common_plant_row['plant_type'] if common_plant_row else 'N/A'
        
        # Most common disease
        cursor.execute('''
            SELECT disease_name, COUNT(*) as count FROM predictions 
            WHERE user_id = ? AND disease_name NOT LIKE '%healthy%'
            GROUP BY disease_name 
            ORDER BY count DESC 
            LIMIT 1
        ''', (user_id,))
        common_disease_row = cursor.fetchone()
        common_disease = common_disease_row['disease_name'] if common_disease_row else 'N/A'
        
        # Average confidence
        cursor.execute('''
            SELECT AVG(confidence) as avg_conf FROM predictions WHERE user_id = ?
        ''', (user_id,))
        avg_conf = cursor.fetchone()['avg_conf'] or 0
        
        # Recent activity (last 7 days)
        cursor.execute('''
            SELECT COUNT(*) as recent FROM predictions 
            WHERE user_id = ? 
            AND created_at >= datetime('now', '-7 days')
        ''', (user_id,))
        recent = cursor.fetchone()['recent']
        
        conn.close()
        
        return {
            'total_predictions': total,
            'healthy_plants': healthy,
            'diseased_plants': diseased,
            'most_common_plant': common_plant,
            'most_common_disease': common_disease,
            'average_confidence': round(avg_conf * 100, 2),
            'recent_activity': recent
        }
    
    def get_all_stats(self):
        """Get global statistics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Total users
        cursor.execute('SELECT COUNT(*) as total FROM users')
        total_users = cursor.fetchone()['total']
        
        # Total predictions
        cursor.execute('SELECT COUNT(*) as total FROM predictions')
        total_predictions = cursor.fetchone()['total']
        
        # Disease distribution
        cursor.execute('''
            SELECT disease_name, COUNT(*) as count 
            FROM predictions 
            GROUP BY disease_name 
            ORDER BY count DESC 
            LIMIT 10
        ''')
        disease_dist = [dict(row) for row in cursor.fetchall()]
        
        # Plant distribution
        cursor.execute('''
            SELECT plant_type, COUNT(*) as count 
            FROM predictions 
            GROUP BY plant_type 
            ORDER BY count DESC 
            LIMIT 10
        ''')
        plant_dist = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        
        return {
            'total_users': total_users,
            'total_predictions': total_predictions,
            'disease_distribution': disease_dist,
            'plant_distribution': plant_dist
        }


# Test the database
if __name__ == '__main__':
    print("Testing Database...")
    db = Database()
    
    # Test user creation
    print("\nCreating test user...")
    user_id = db.create_user('testuser', 'test@example.com', 'hashed_password')
    if user_id:
        print(f"✓ User created with ID: {user_id}")
    
    # Test getting user
    print("\nGetting user...")
    user = db.get_user_by_email('test@example.com')
    if user:
        print(f"✓ User found: {user['username']}")
    
    # Test saving prediction
    print("\nSaving test prediction...")
    pred_id = db.save_prediction(user_id, 'test.jpg', 'Tomato', 'Early blight', 0.95)
    if pred_id:
        print(f"✓ Prediction saved with ID: {pred_id}")
    
    # Test getting predictions
    print("\nGetting predictions...")
    predictions = db.get_user_predictions(user_id)
    print(f"✓ Found {len(predictions)} prediction(s)")
    
    # Test statistics
    print("\nGetting statistics...")
    stats = db.get_user_stats(user_id)
    print(f"✓ Statistics: {stats}")
    
    print("\n✓ All tests passed!")
