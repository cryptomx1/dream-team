import sys
import os

# Add the parent directory to the Python path to import middleware
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from middleware import app

# Vercel expects the Flask app to be available as 'app'
# No additional wrapper needed for modern Vercel Python runtime