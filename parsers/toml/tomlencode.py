from toml import dumps

class TomlEncoder:
   def encode(self, obj):
       return dumps(obj)