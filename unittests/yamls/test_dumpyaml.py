import unittest
import sys

sys.path.append(sys.path[0] + "/../..")
from parsers import YamlParser
import yaml


obj_test = [True, False, { "str": 1, "my": [ None, 1.24124, -1, 0, ]}]

class DumpPickle(unittest.TestCase):

    def test_dump(self):
        s = YamlParser.dumps(obj_test)
        self.assertEqual(yaml.load(s), obj_test)
        


if __name__ == "__main__":
    unittest.main()
