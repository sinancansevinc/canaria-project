import redis

class RedisConnector:
    def __init__(self, host='scrapyredis', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def is_item_cached(self, item_id):
        return self.client.exists(item_id)

    def cache_item(self, item_id, item_data):
        self.client.set(item_id, item_data)

    def close(self):
        self.client.close()

