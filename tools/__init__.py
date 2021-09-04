from .packing import packing
from .unpacking import unpacking

class Packager:

    def __init__(self, parser, pack = packing, unpack = unpacking):
        self.parser = parser
        self.pack = pack
        self.unpack = unpack

    def dumps(self, obj):
        return self.parser.dumps(self.unpack(obj))

    def dump(self, obj, file):
        return self.parser.dump(self.unpack(obj), file)

    def loads(self, obj):
        return self.pack(self.parser.loads(obj))

    def load(self, file):
        return self.pack(self.parser.load(file))


