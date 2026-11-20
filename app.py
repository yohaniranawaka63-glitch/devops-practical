
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World! V3!"

if __name__ == '__main__':
    # Render dynamic port or local default port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
