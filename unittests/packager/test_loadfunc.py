# import unittest
# import sys

# sys.path.append(sys.path[0] + "/../..")
# from tools.packing import packing
# import math as m
# from json import loads


# def sum(x, y):
#     return x + y


# def something(x, y):
#     c = 3
#     return x * y / c


# def module_add(x, y):
#     return m.sin(x + y)


# def func_in_func(x, y):
#     def f(x, y):
#         return x + y

#     return m.sin(f(x, y)) ** 33


# def get_json_sum():
#     fp = open("unittests/objects/packager/sum.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


# def get_json_something():
#     fp = open("unittests/objects/packager/something.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


# def get_json_module_add():
#     fp = open("unittests/objects/packager/module_add.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


# def get_json_func_in_func():
#     fp = open("unittests/objects/packager/func_in_func.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


# class LoadFunc(unittest.TestCase):
#     def test_func_only(self):
#         self.assertEqual(packing(loads(get_json_sum()))(5, 6), sum(5, 6))
#         self.assertEqual(
#             packing(loads(get_json_something()))(5, 6), something(5, 6)
#         )

#     def test_add_module(self):
#         self.assertEqual(
#             packing(loads(get_json_module_add()))(5, 6), module_add(5, 6)
#         )

#     # def test_func_in_func(self):
#     #     self.assertEqual(
#     #         packing(loads(get_json_func_in_func()))(5, 6), func_in_func(5, 6)
#     #     )


# if __name__ == "__main__":
#     unittest.main()
