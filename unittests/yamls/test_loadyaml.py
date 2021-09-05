import unittest
import sys

sys.path.append(sys.path[0] + "/../..")
from parsers import YamlParser
import yaml


obj_test = [True, False, { "str": 1, "my": [ None, 1.24124, 532, ]}]

class LoadToml(unittest.TestCase):
    pass

    def test_dump(self):
        s = yaml.dump(obj_test)
        self.assertEqual(YamlParser.loads(s), obj_test)


if __name__ == "__main__":
    unittest.main()

