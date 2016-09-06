from app import app
import os

version = os.getenv('VERSION_STR', '0.1.2')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! " + version
