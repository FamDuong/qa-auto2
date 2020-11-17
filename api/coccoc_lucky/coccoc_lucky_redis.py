import re
import json
import inspect
from rediscluster import RedisCluster
from datetime import date
from config.environment import COCCOC_LUCKY_REDIS_HOST
from config.environment import COCCOC_LUCKY_REDIS_POST
from config.environment import COCCOC_LUCKY_REDIS_PASSWORD
#import serialized_redis
import logging
LOGGER = logging.getLogger(__name__)

class LuckyRedis:
    # Enable cluster mode
    def redis_cli_init_cluster(self):
        startup_nodes = [{"host": COCCOC_LUCKY_REDIS_HOST, "port": COCCOC_LUCKY_REDIS_POST}]
        redis_cli = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, password=COCCOC_LUCKY_REDIS_PASSWORD, skip_full_coverage_check=True)
        # redis_cli = serialized_redis.JSONSerializedRedis(host=COCCOC_LUCKY_REDIS_HOST, port=COCCOC_LUCKY_REDIS_POST, password=COCCOC_LUCKY_REDIS_PASSWORD, db=0)
        redis_cli.ping()
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
    def redis_get(self, query, format_data="json"):
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
        LOGGER.info("%s: %s" % (query, data))
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

    # Delete a key
    def redis_delete(self, query):
        try:
            redis_cli = self.redis_cli_init_cluster()
            redis_cli.delete(query)
        except Exception as e:
            print(e)
            exit('Failed to connect, terminating.')
        finally:
            del redis_cli

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
        print("    ", function_name, ": ", string)

    def get_lucky_key(self, key):
        lucky_key = "coccoc-lucky-dev:coccoc_lucky_cache:" + str(key)
        print("Key: %s" % lucky_key)
        return lucky_key

    def get_lucky_today_key(self, key):
        today = date.today()
        today = today.strftime("%Y_%m_%d")
        lucky_key = "lucky-draw-dev:lucky_draw_cache:" + key + "_" + today
        print("Key: %s" % lucky_key)
        return lucky_key

    # Convert lucky redis data to dic
    def convert_redis_data_to_dic(self, data, type="USER_CHECKIN"):
        data = data.replace(chr(0), "")
        data = re.sub(";i:", " : ", data)
        if type == "USER_CHECKIN":
            data = data.replace(r"App\Entities\UserCheckInEntity", "")
            data = re.sub("ip\";s:[0-9]*:\"", 'ip\" : \"', data)
            data = re.sub("userAgent\";s:[0-9]*:\"", 'userAgent\" : \"', data)
            data = re.sub("checkInDate\";s:[0-9]*:\"", 'checkInDate\" : \"', data)
        elif type == "CONFIGS":
            data = data.replace(r"App\Entities\ConfigEntity", "")
            data = re.sub("name\";s:[0-9]*:\"", 'name\" : \"', data)
            data = re.sub("value\";s:[0-9]*:\"", 'value\" : \"', data)
            data = re.sub("description\";s:[0-9]*:\"", 'description\" : \"', data)
        elif type == "COLLECTIONS":
            data = data.replace(r"App\Entities\CollectionEntity", "")
            data = re.sub("name\";s:[0-9]*:\"", 'name\" : \"', data)
            data = re.sub("imageUrl\";s:[0-9]*:\"", 'imageUrl\" : \"', data)
            data = re.sub("description\";s:[0-9]*:\"", 'description\" : \"', data)
            start = data.find("\"prizeIdArray") + len("{") - 1
            end = data.find("}}") + 1
            substring = data[start:end]
            data = data.replace(substring, '')
        data = re.sub(";s:[0-9]*:", ' , ', data)
        data = re.sub("s:[0-9]*:", "", data)
        data = re.sub(";", "", data)
        start = data.find("{") + len("{") - 1
        end = data.find("}") + 1
        substring = data[start:end]
        data = substring
        self.print_debug(data)
        # Convert to dic
        data_dict = eval(data)
        return data_dict
