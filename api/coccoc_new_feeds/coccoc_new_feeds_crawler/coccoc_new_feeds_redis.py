import redis
import json
import inspect
from rediscluster import RedisCluster

from config.environment import COCCOC_NEW_FEED_REDIS_HOST
from config.environment import COCCOC_NEW_FEED_REDIS_PORT
from config.environment import COCCOC_NEW_FEED_REDIS_PASSWORD
from config.environment import COCCOC_NEW_FEED_REDIS_NODES

class NewsFeedRedis:
    # Enable cluster mode
    def redis_cli_init_cluster(self):
        init_host = COCCOC_NEW_FEED_REDIS_HOST.replace("{i}", "0")
        startup_nodes = [{"host": init_host, "port": COCCOC_NEW_FEED_REDIS_PORT}]
        redis_cli = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, password=COCCOC_NEW_FEED_REDIS_PASSWORD, skip_full_coverage_check=True)
        redis_cli.ping()
        return redis_cli

    # Disable cluster mode
    def redis_cli_init_strict(self, node = 0):
        print("Redis: CONNECT TO NODE %d" % node)
        redis_cli = redis.StrictRedis(host=COCCOC_NEW_FEED_REDIS_HOST.replace("{i}", str(node)), port=COCCOC_NEW_FEED_REDIS_PORT, db=0,
                                      password=COCCOC_NEW_FEED_REDIS_PASSWORD)
        return redis_cli

    # Get members
    def redis_smembers(self, query):
        try:
            redis_cli = self.redis_cli_init_cluster()
            # redis_cli.ping()
            data = redis_cli.smembers(query)
            return list(data)
        except Exception as e:
            print(e)
            exit('Failed to connect, terminating.')
        finally:
            del redis_cli

    # Get keys in all nodes and returns as list
    def redis_keys(self, query):
        data = []
        # Scan all nodes
        try:
            redis_cli = self.redis_cli_init_cluster()
            # redis_cli.ping()
            data_nodes = redis_cli.keys(query)
            data += data_nodes
            # return list(data)
        except Exception as e:
            print(e)
            exit('Failed to connect, terminating.')
        finally:
            del redis_cli
        return data

    # Get a key in all nodes and return
    def redis_get(self, query, format_data ="json"):
        data = []
        try:
            redis_cli = self.redis_cli_init_cluster()
            # redis_cli.ping()
            data = redis_cli.get(query)
            if format_data == "json":
                data = self.convert_to_json(data)
        except Exception as e:
            print(e)
            exit('Failed to connect, terminating.')
        finally:
            del redis_cli
        return data

    # Get a key in all nodes and return
    def redis_lrange(self, name, start=0, end=-1, format_data="json"):
        data = []
        try:
            redis_cli = self.redis_cli_init_cluster()
            # redis_cli.ping()
            data = redis_cli.lrange(name, start=start, end=end)
            if format_data == "json":
                data = self.convert_to_json(data)
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

    def convert_to_json(self, data):
        try:
            data = json.loads(data)
        except:
            # print("ERROR: Cannot convert data")
            self.print_debug("ERROR: Cannot convert data")
        return data


    def print_debug(self, string):
        function_name = inspect.stack()[1].function
        print(function_name, ": ", string)