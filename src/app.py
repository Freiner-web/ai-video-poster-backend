from flask import Flask
from src import auth

app = Flask(__name__)

# Register authentication routes
auth.register_routes(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
