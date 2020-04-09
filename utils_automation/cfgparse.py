import configparser


class CfgParse:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_testrail_config(self):
        config = configparser.ConfigParser()
        config.read(filenames=self.file_name)
        return config
















