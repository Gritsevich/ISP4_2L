import builtins
import inspect
import types

def create_code(obj):
    return types.CodeType(
        obj["co_argcount"],
        obj["co_posonlyargcount"],
        obj["co_kwonlyargcount"],
        obj["co_nlocals"],
        obj["co_stacksize"],
        obj["co_flags"],
        bytes(obj["co_code"]),
        tuple(packing(obj["co_consts"])),
        tuple(obj["co_names"]),
        tuple(obj["co_varnames"]),
        obj["co_filename"],
        obj["co_name"],
        obj["co_firstlineno"],
        bytes(obj["co_lnotab"]),
        tuple(obj["co_freevars"]),
        tuple(obj["co_cellvars"]),
    )

def packing(obj):
    if isinstance(obj, (int, float, type(None), bool)):
        return obj
    if isinstance(obj, (list, set, tuple)):
        return [packing(i) for i in obj]
    if isinstance(obj, str):
        if obj.startswith("<module "):
            return __import__(obj.split("'")[1])
        else: 
            return obj
    if isinstance(obj, dict):
        if "function" in obj:
            obj = obj["function"]
            gls = { key : packing(value) for key, value in obj["globals"].items()}
            gls['__builtins__'] = __builtins__
            return types.FunctionType(create_code(obj["co"]), gls)
        else: 
            return {packing(key) : packing(value) for key, value in obj.items()}

    raise ValueError("underfind type!")