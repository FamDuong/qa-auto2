import yaml


class YamlUtils:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(YamlUtils, cls).__new__(cls)

        return cls.instance

    def read_data_from_file(self, file):
        with open(file) as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def write_data_to_file(self, loaded, file):
        with open(file, 'wb') as stream:
            try:
                return yaml.safe_dump(loaded, stream, default_flow_style=False
                                      , explicit_start=True, allow_unicode=True, encoding='utf-8')
            except yaml.YAMLError as exc:
                print(exc)


class TxtUtils:

    def write_string_to_text_file(self, file, string_value):
        import codecs
        with codecs.open(file, 'w', 'utf-8') as f:
            f.write(string_value)

    def read_text_file(self, file):
        import codecs
        with codecs.open(file, 'r', 'utf-8') as f:
            return f.read()



