import inspect
from types import ModuleType

def rec_list(obj):
    return [unpacking(i) for i in obj]

def rec_dict(obj):
    return {unpacking(i) : unpacking(obj[i]) for i in obj}

def rec_code(obj):
    sat = {}
    for i in dir(obj):
        if i.startswith("co_"):
           sat[i] = unpacking(getattr(obj, i))
    return sat

def rec_method(obj):
    mas = {}
    sat = rec_code(obj.__code__)
    for i in obj.__code__.co_names:
        if i in obj.__globals__:
            mas[i] = unpacking(obj.__globals__[i])  
    return {"function":{"globals":mas,"co": sat}}   

def unpacking(obj):
    if isinstance(obj, (int, float, str, type(None), bool)):
        return obj
    if isinstance(obj,(list, tuple, set)):
        return rec_list(obj)
    if isinstance(obj, dict):
        return rec_dict(obj)
    if inspect.isfunction(obj):
        return rec_method(obj)
    if isinstance(obj, ModuleType):
        return str(obj)
    if inspect.iscode(obj):
        return rec_code(obj)
    if isinstance(obj, bytes):
        return list(obj)
    raise TypeError("This type doesn't exist " + str(type(obj)))


