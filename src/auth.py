from flask import request, jsonify

# In-memory user store (for demonstration purposes)
users = {}
# To be replaced with a proper database

def register_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        if username in users:
            return jsonify({'message': 'User already exists'}), 400

        users[username] = {'password': password}
        return jsonify({'message': 'User registered successfully'}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        user = users.get(username)
        if not user or user['password'] != password:
            return jsonify({'message': 'Invalid credentials'}), 401

        return jsonify({'message': 'Login successful'}), 200
