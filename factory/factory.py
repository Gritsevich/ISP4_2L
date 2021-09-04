from tools import Packager
from parsers import JsonParser, YamlParser, TomlParser



class Serializer:

    def __init__(self, packanger = Packager):
        self.packager = packanger
        self.parsers = { "JSON": JsonParser,
                        "YAML": YamlParser,
                        "TOML": TomlParser,
        }

    def add_parser(self, name, parser):
        self.parsers[name.upper()] = parser

    def get_parser(self, name):
        parser = self.parsers.get(name.upper())
        if parser == None:
            raise NameError("Underfind parser")

        return self.packager(parser)
