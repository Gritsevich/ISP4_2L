class YamlDecoder:
    int_const = tuple("1 2 3 4 5 6 7 8 9 0".split(" "))

    def __init__(self):
        self.yaml_to_true = self.yaml_to_custom("true", True);
        self.yaml_to_false = self.yaml_to_custom("false", False);
        self.yaml_to_none = self.yaml_to_custom("null", None);

        self.yaml_types = [
            ("-", self.yaml_to_list),
            ('"', self.yaml_to_string),
            (self.int_const, self.yaml_to_numeric),
            ("false", self.yaml_to_false),
            ("true", self.yaml_to_true),
            ("null", self.yaml_to_none)
        ]

    def yaml_to_custom(self, word, value=None):
        def custom_conversion(obj):
            if obj.startswith(word):
                return value, obj[len(word):]

        custom_conversion.__name__ = "parse_%s" % word
        return custom_conversion

    def yaml_to_dict(self, objs):
        res = {}
        while self.check_for_dict(objs):
            key = self.yaml_to_obj(objs[:objs.find(":")])[0]
            objs = objs[objs.find(":") + 1:]
            value, objs = self.yaml_to_obj(objs)
            res[key] = value
        return res, objs.lstrip()

    def yaml_to_list(self, objs):
        res = []
        while objs.startswith("-"):
            objs = remove_prefix(objs, "-")
            key, objs = self.yaml_to_obj(objs)
            res.append(key)
            pos = objs.find("\n") + 1
            if pos == 0:
                return res, ""
            objs = objs[pos:].lstrip()
        return res, objs

    def yaml_to_numeric(self, obj):
        for i in range(len(obj)):
            if obj[i] not in self.int_const and obj[i] != ".":
                try:
                    return int(obj[:i]), obj[i:]
                except ValueError:
                    return float(obj[:i]), obj[i:]

        return int(obj[:i + 1]), obj[i + 1:]

    def yaml_to_string(self, obj):
        obj = remove_prefix(obj, '"')
        tmp = obj.find('"')
        obj_bound = obj[tmp + 1:]
        return obj[:tmp], obj[tmp + 1:]

    def check_for_dict(self, obj) -> bool:
        pos = obj.find("\n")
        if pos == -1:
            pos = len(obj) + 1
        if obj.find(":", 0, pos) != -1:
            return True
        return False

    def yaml_to_obj(self, obj):
        obj = obj.lstrip()
        if self.check_for_dict(obj):
            return self.yaml_to_dict(obj)
        if obj.startswith("[]"):
            return list(), remove_prefix(obj, "[]")
        for (char, func) in self.yaml_types:
            if not obj:
                pass
            elif obj.startswith(char):
                return func(obj)

        return obj, ""

        raise ValueError(str(obj.split(",")) + " is not supported!")

    def decode(self, obj):
        (item, obj) = self.yaml_to_obj(obj)
        obj = obj.lstrip()
        if obj != "":
            raise ValueError("Wrong format!")
        else:
            return item


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text