import redis
from rediscluster import RedisCluster

from config.environment import COCCOC_NEW_FEED_REDIS_HOST
from config.environment import COCCOC_NEW_FEED_REDIS_PORT
from config.environment import COCCOC_NEW_FEED_REDIS_PASSWORD
from config.environment import COCCOC_NEW_FEED_REDIS_NODES

class NewFeedRedis:
    # T.B.D: Need to enable cluster mode
    def redis_cli_init_cluster(self):
        startup_nodes = [{"host": COCCOC_NEW_FEED_REDIS_HOST, "port": COCCOC_NEW_FEED_REDIS_PORT}]

        redis_cli = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        return redis_cli

    def redis_cli_init_strict(self, node = 0):
        print("Redis: CONNECT TO NODE %d" % node)
        redis_cli = redis.StrictRedis(host=COCCOC_NEW_FEED_REDIS_HOST.replace("{i}", str(node)), port=COCCOC_NEW_FEED_REDIS_PORT, db=0,
                                      password=COCCOC_NEW_FEED_REDIS_PASSWORD)
        return redis_cli

    # Get members
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

    # Get keys in all nodes and returns as list
    def get_redis_keys(self, query):
        data = []
        # Scan all nodes
        for i in range(COCCOC_NEW_FEED_REDIS_NODES):
            try:
                redis_cli = self.redis_cli_init_strict(i)
                redis_cli.ping()
                data_nodes = redis_cli.keys(query)
                data_nodes = self.convert_byte_to_string(list(data_nodes))
                data += data_nodes
                # return list(data)
            except Exception as e:
                print(e)
                exit('Failed to connect, terminating.')
            finally:
                del redis_cli
        return data

    # Convert all items in list to string
    def convert_byte_to_string(self, list):
        encoding = 'utf-8'
        convert_list = [i.decode(encoding) for i in list]
        return convert_list