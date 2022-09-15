from CTypeGen import generate, PythonType
from ctypes import *


generate(["libbasic.so"], "basic.py", [PythonType("SomeStructure")], ["someFunction"])
# lib = cdll.powrprof
# decorateFunctions(lib)

# print(lib)