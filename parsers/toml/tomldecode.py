from toml import loads

class TomlDecoder:
   def decode(self, obj):
       return loads(obj)