import redis

redis_db = redis.Redis(host='localhost', port=6379)

# Set the initial user count
redis_db.set('user_count', 10)

# Add sample user IDs
user_ids = {
    '1': 'John',
    '2': 'Jane',
    '3': 'Mike',
    '4': 'Sarah',
}

# Set user IDs in Redis
for user_id, user_name in user_ids.items():
    redis_db.set(user_id, user_name)

print("Initial values added to Redis database.")
