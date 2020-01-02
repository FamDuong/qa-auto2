import yaml


class YamlCustom:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(YamlCustom, cls).__new__(cls)

        return cls.instance

    def read_data_from_file(self, file):
        with open(file) as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)





