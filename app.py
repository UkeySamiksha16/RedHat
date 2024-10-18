Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask
... import os
... 
... app = Flask(__name__)
... 
... @app.route('/')
... def hello():
...     return "Hello World!"
... 
... if __name__ == '__main__':
...     port = os.environ.get('FLASK_PORT') or 8080
...     port = int(port)
... 
