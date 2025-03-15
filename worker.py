import redis
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(filename='/data/hits.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Connect to Redis
try:
    redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
except redis.ConnectionError as e:
    logging.error(f"Redis connection error: {e}")
    exit(1)

# Initialize hit counter
hit_count = 0

# Configurable sleep interval
SLEEP_INTERVAL = 1  # seconds

while True:
    try:
        hit = redis_client.lpop('page_hits')
        if hit:
            hit_count += 1  # Increment the hit counter
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"Page hit #{hit_count} recorded at {timestamp}.")
    except Exception as e:
        logging.error(f"Error while processing hits: {e}")

    time.sleep(SLEEP_INTERVAL)
