#!/usr/bin/env python

from parsers import JsonParser, YamlParser, TomlParser

types = {
    "yaml": YamlParser,
    "json": JsonParser,
    "toml": TomlParser,
}


def dump(in_file, out_file):
    obj = types[in_file.split(".")[-1].lower()].load(in_file)
    types[out_file.split(".")[-1].lower()].dump(obj, out_file)
