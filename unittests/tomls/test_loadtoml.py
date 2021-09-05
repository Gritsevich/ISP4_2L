import unittest
import sys

sys.path.append(sys.path[0] + "/../..")
from parsers import TomlParser
import toml


class LoadToml(unittest.TestCase):

    obj_test = { "str": { "str": 1, "my": [None, 0]}}

    # def test_dump(self):
    #     s = toml.dumps(self.obj_test)
    #     self.assertEqual(TomlParser.loads(s), self.obj_test)


if __name__ == "__main__":
    unittest.main()

