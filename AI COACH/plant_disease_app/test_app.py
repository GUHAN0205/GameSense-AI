"""
Simple test script to verify the application setup
"""

import os
import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing module imports...")
    print("-" * 50)
    
    modules = [
        ('Flask', 'flask'),
        ('Werkzeug', 'werkzeug'),
        ('PIL (Pillow)', 'PIL'),
        ('NumPy', 'numpy'),
        ('TensorFlow', 'tensorflow')
    ]
    
    failed = []
    
    for name, module in modules:
        try:
            __import__(module)
            print(f"✓ {name} - OK")
        except ImportError as e:
            print(f"✗ {name} - FAILED: {e}")
            failed.append(name)
    
    print("-" * 50)
    
    if failed:
        print(f"\n❌ Failed to import: {', '.join(failed)}")
        print("\nRun: pip install -r requirements.txt")
        return False
    else:
        print("\n✓ All imports successful!")
        return True

def test_directories():
    """Test if required directories exist"""
    print("\nTesting directories...")
    print("-" * 50)
    
    directories = [
        'uploads',
        'static',
        'static/css',
        'static/js',
        'static/images',
        'templates'
    ]
    
    failed = []
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"✓ {directory}/ - EXISTS")
        else:
            print(f"✗ {directory}/ - MISSING")
            failed.append(directory)
    
    print("-" * 50)
    
    if failed:
        print(f"\n❌ Missing directories: {', '.join(failed)}")
        print("\nCreating missing directories...")
        for directory in failed:
            os.makedirs(directory, exist_ok=True)
            print(f"Created: {directory}/")
        return True
    else:
        print("\n✓ All directories exist!")
        return True

def test_files():
    """Test if required files exist"""
    print("\nTesting files...")
    print("-" * 50)
    
    files = {
        'app.py': 'Main application file',
        'database.py': 'Database module',
        'requirements.txt': 'Dependencies list',
        'templates/base.html': 'Base template',
        'templates/index.html': 'Home page template',
        'static/css/style.css': 'Stylesheet',
        'static/js/main.js': 'JavaScript file'
    }
    
    failed = []
    
    for file, description in files.items():
        if os.path.exists(file):
            print(f"✓ {file} - OK ({description})")
        else:
            print(f"✗ {file} - MISSING ({description})")
            failed.append(file)
    
    print("-" * 50)
    
    if failed:
        print(f"\n❌ Missing files: {', '.join(failed)}")
        return False
    else:
        print("\n✓ All required files exist!")
        return True

def test_database():
    """Test database initialization"""
    print("\nTesting database...")
    print("-" * 50)
    
    try:
        from database import Database
        db = Database('test_plant_disease.db')
        print("✓ Database module imported")
        print("✓ Database initialized")
        
        # Clean up test database
        if os.path.exists('test_plant_disease.db'):
            os.remove('test_plant_disease.db')
            print("✓ Test database cleaned up")
        
        print("-" * 50)
        print("\n✓ Database test passed!")
        return True
    except Exception as e:
        print(f"✗ Database test failed: {e}")
        print("-" * 50)
        return False

def test_model():
    """Test if model file exists"""
    print("\nTesting model file...")
    print("-" * 50)
    
    model_file = 'plant_disease_model.h5'
    
    if os.path.exists(model_file):
        size = os.path.getsize(model_file) / (1024 * 1024)
        print(f"✓ {model_file} found ({size:.2f} MB)")
        print("  The app will use the trained model")
    else:
        print(f"ℹ {model_file} not found")
        print("  The app will use mock predictions")
        print("  This is OK for testing!")
    
    print("-" * 50)
    return True

def main():
    """Run all tests"""
    print("\n" + "="*50)
    print("Plant Disease Detection - System Test")
    print("="*50 + "\n")
    
    tests = [
        ("Module Imports", test_imports),
        ("Directories", test_directories),
        ("Required Files", test_files),
        ("Database", test_database),
        ("Model File", test_model)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*50)
    print("Test Summary")
    print("="*50 + "\n")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status} - {test_name}")
    
    print("\n" + "-"*50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✅ All tests passed! You're ready to run the app!")
        print("\nNext steps:")
        print("1. Run: python app.py")
        print("2. Open: http://localhost:5000")
        print("3. Start detecting plant diseases!")
    else:
        print("\n⚠️ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Run: pip install -r requirements.txt")
        print("- Check if all files are present")
        print("- Read SETUP_GUIDE.md for detailed instructions")
    
    print("\n" + "="*50 + "\n")

if __name__ == '__main__':
    main()
