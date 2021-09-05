import unittest
import sys

sys.path.append(sys.path[0] + "/../..")
from parsers import JsonParser
from json import dumps

class LoadJSON(unittest.TestCase):

    obj_test = [True, False, { "str": 1, "my": [ None, 1.24124, -1, 0, ]}]

    def test_dump(self):
        s = dumps(self.obj_test)
        self.assertEqual(JsonParser.loads(s), self.obj_test)
