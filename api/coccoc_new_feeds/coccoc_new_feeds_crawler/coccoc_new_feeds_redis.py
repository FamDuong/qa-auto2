import redis

from config.environment import COCCOC_NEW_FEED_REDIS_HOST
from config.environment import COCCOC_NEW_FEED_REDIS_PORT
from config.environment import COCCOC_NEW_FEED_REDIS_PASSWORD

class NewFeedRedis:

    def get_redis_smembers(self, query):
        try:
            redis_cli = redis.StrictRedis(host=COCCOC_NEW_FEED_REDIS_HOST, port=COCCOC_NEW_FEED_REDIS_PORT, db=0, password=COCCOC_NEW_FEED_REDIS_PASSWORD)
            redis_cli.ping()
            data = redis_cli.smembers(query)
            return list(data)
        except Exception as e:
            print(e)
            exit('Failed to connect, terminating.')
        finally:
            del redis_cli
