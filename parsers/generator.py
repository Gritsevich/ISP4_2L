class Parser:
    def __init__(self, decode, encode):
        self.decode = decode
        self.encode = encode

    def dumps(self, obj):
        return self.encode(obj)

    def dump(self, obj, file):
        f = open(file, "w")
        s = self.encode(obj)
        f.write(s)
        f.close()

    def loads(self, s):
        return self.decode(s)

    def load(self, file):
        f = open(file, "r")
        res = self.decode(f.read())
        f.close()
        return res