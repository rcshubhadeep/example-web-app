from app import app
import os

version = os.getenv('VERSION_STR', '0.4.10')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! " + version
    # @TODO we really need to do something in the db here too as its another
    #       image and we want to show that they are hooked together.
