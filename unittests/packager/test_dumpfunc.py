# import unittest
# import sys

# sys.path.append(sys.path[0] + "/../..")
# from tools.unpacking import unpacking
# import math as m
# from json import loads


# def func():
#     pass


# def hello():
#     print("Hello, World!")


# def params(x):
#     print(x)


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


# def get_json_func():
#     fp = open("unittests/objects/packager/func.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


# def get_json_hello():
#     fp = open("unittests/objects/packager/hello.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


# def get_json_params():
#     fp = open("unittests/objects/packager/params.json", "r")
#     res = fp.read()
#     fp.close()
#     return res


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

# class DumpFunc(unittest.TestCase):
#     def test_func_only(self):
#         self.assertEqual(unpacking(func), loads(get_json_func()))
#         self.assertEqual(unpacking(hello), loads(get_json_hello()))
#         self.assertEqual(unpacking(params), loads(get_json_params()))
#         self.assertEqual(unpacking(sum), loads(get_json_sum()))
#         self.assertEqual(
#             unpacking(something), loads(get_json_something())
#         )

#     def test_add_module(self):
#         self.assertEqual(
#             unpacking(module_add), loads(get_json_module_add())
#         )

#     def test_func_in_func(self):
#         self.assertEqual(
#             unpacking(func_in_func), loads(get_json_func_in_func())
#         )


# if __name__ == "__main__":
#     unittest.main()
