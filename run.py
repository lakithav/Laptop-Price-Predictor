"""
Launcher script for Render deployment
Changes to website directory and starts the Flask app with Gunicorn
"""
import os
import sys

# Change to website directory where app.py is located
os.chdir('website')

# Add website directory to Python path
sys.path.insert(0, os.getcwd())

# Import and run the app with Gunicorn programmatically
from gunicorn.app.base import BaseApplication

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    from app import app
    
    options = {
        'bind': f"0.0.0.0:{os.environ.get('PORT', '5000')}",
        'workers': 1,
        'timeout': 120,
    }
    
    StandaloneApplication(app, options).run()
