Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask
... app = Flask(__name__)
... @app.route('/')
... def index():
...  return '<h1>Hello WSB! Greetings from Flask!</h1>'
... if __name__ == "__main__":
