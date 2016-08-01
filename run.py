from app import app
import os

host_name = os.getenv('HOST_NAME', '0.0.0.0')

app.run(debug=True, host=host_name)
