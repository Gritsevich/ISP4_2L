from .generator import Parser
from .json import JsonEncoder, JsonDecoder
from .yaml import YamlEncoder, YamlDecoder
from .toml import TomlEncoder, TomlDecoder

JsonParser = Parser(JsonDecoder().decode, JsonEncoder().encode)
YamlParser = Parser(YamlDecoder().decode, YamlEncoder().encode)
TomlParser = Parser(TomlDecoder().decode, TomlEncoder().encode)