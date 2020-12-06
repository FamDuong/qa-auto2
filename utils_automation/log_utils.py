import inspect

import logging
LOGGER = logging.getLogger(__name__)

class LogUtils():

    def print_debug(self, string):
        function_name = inspect.stack()[1].function
        print(function_name, ": ", string)

