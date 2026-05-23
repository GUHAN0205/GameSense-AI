"""
Script to create a ZIP file of the plant disease detection project
"""

import os
import zipfile
from datetime import datetime

def create_project_zip():
    """Create a ZIP file containing all project files"""
    
    # Project name and timestamp
    project_name = "plant_disease_app"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"{project_name}_{timestamp}.zip"
    
    # Files and folders to include
    include_patterns = [
        '*.py',
        '*.txt',
        '*.md',
        '*.h5',  # Model file
        'templates/*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/images/*.*',
        '.gitignore',
        'README.md'
    ]
    
    # Folders to exclude
    exclude_folders = [
        '__pycache__',
        'venv',
        'env',
        '.git',
        'uploads',
        '*.db'
    ]
    
    print(f"Creating ZIP file: {zip_filename}")
    print("="*50)
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        file_count = 0
        
        for root, dirs, files in os.walk('.'):
            # Remove excluded folders
            dirs[:] = [d for d in dirs if d not in exclude_folders]
            
            for file in files:
                # Skip certain files
                if file.endswith(('.pyc', '.db', '.zip')):
                    continue
                
                file_path = os.path.join(root, file)
                arcname = file_path[2:]  # Remove './' from path
                
                zipf.write(file_path, arcname)
                file_count += 1
                print(f"Added: {arcname}")
    
    file_size = os.path.getsize(zip_filename) / (1024 * 1024)  # Size in MB
    
    print("="*50)
    print(f"✓ ZIP file created successfully!")
    print(f"  Name: {zip_filename}")
    print(f"  Size: {file_size:.2f} MB")
    print(f"  Files: {file_count}")
    print("\nYou can now share this ZIP file or deploy it to a server.")

if __name__ == '__main__':
    create_project_zip()
