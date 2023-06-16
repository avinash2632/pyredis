from flask import Flask, jsonify
import redis

app = Flask(__name__)
redis_db = redis.Redis(host='localhost', port=6379)

# Add sample user IDs and names to Redis
def add_sample_users():
    user_ids = {
        '1': 'John',
        '2': 'Jane',
        '3': 'Mike',
        '4': 'Sarah',
    }
    for user_id, user_name in user_ids.items():
        redis_db.set(user_id, user_name)

# API endpoint to get the names of all users
@app.route('/users', methods=['GET'])
def get_user_names():
    user_keys = redis_db.keys('*')
    user_names = [redis_db.get(key).decode('utf-8') for key in user_keys]
    return jsonify({'names': user_names})

# API endpoint to retrieve user name by ID
@app.route('/<id>', methods=['GET'])
def get_user_name(id):
    user_name = redis_db.get(id)
    if user_name:
        return jsonify({'name': user_name.decode('utf-8')})
    else:
        return jsonify({'message': 'User not found'})

if __name__ == '__main__':
    # Add initial user values to Redis
    add_sample_users()

    # Start the Flask application
    app.run()
