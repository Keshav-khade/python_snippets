# python special variables and attributes

# def func(a,b):
#    print(a + b)
# func(8, 9)
# func.__call__(8,9)

"""
# __builtins__ -> 
          this is a special variable in python that holds a reference for builtin namespace
          this builtin module or namespace contains all the variables and functions that are available for day to day usage
          like print() , input() , len() etc.
          and can be used directly without any import
          without it you have to implement your logic for print() , and len() functions
          it simplifies coding, by providing optimized builtin functions

import builtins # module in python for all builtin functions

print(dir(builtins))

print(builtins.len([1,2,3,4,5]))
builtins.print("Hello world") 
print(type(builtins)) # <class 'module'>
"""

"""
__doc__ -> extracts documents or docstring created in a module like in functions, classes, and in script block

def greet():
    '''This function greets the user.'''
    print("Hello")
print(greet.__doc__)   # This function greets the user.

__file__ -> 
gives us the exact path for current file in which it used
stores the file path of the module currently running.

# in a file called prog31.py
print(__file__)   # prints something like: d:\c and cpp\DSA_placement_series\modules.py

"""

"""
3. __name__
This tells you the name of the current module.
If you run a file directly → __name__ becomes "__main__".
If you import that file into another file → __name__ becomes the filename (without .py).

example ->
print("in prog31 module")
print("thank you")

if __name__ == '__main__':
          print("module executed directly", __name__)
else:
          print("module executed thru another module indirectly", __name__)
"""

"""
__spec__ -> 
1. it tells the specifications about modules how it's loading, name of module , origin of that module
2. an object holding loading info (name, loader, origin, etc.)

import math
print(math.__spec__) # overall information

print(math.__spec__.loader) Tells you the loader class used to import this module — i.e., the internal Python 
                            mechanism responsible for bringing this module into memory.
                            builtinimporter object will load builtin module for execution
                            the loader object responsible for executing the module

print(math.__spec__.name) # qualified name of that module / Just the name of the module, taken from its spec.

print(math.__spec__.origin) 
# Tells you where the module came from — a file path for your own modules, or the string "built-in" for built-in modules like math.
the structural path to the source file if it user defined and built-ins for builtin module

__loader__ → 
1. tells you which loader (mechanism) Python used to load this module.
2. contains the actual loader object that the python import system used to load and initialize a module.
3. python attaches this loader object to the module as __loader__ for runtime introspection and troubleshooting


import math
import sys
import modules
# print(sys.__spec__)
print(math.__spec__.loader)
print()
print(modules.__spec__.loader) #because it's loaded from an actual .py source file on disk.
"""

"""
5. __main__
This is the name Python gives to the top-level script that you run directly (as opposed to a module you import). It's literally the string "__main__" — not something you write, but something Python assigns.

if __name__ == "__main__":
    print("This file was run directly")
"""

"""
The core idea behind __init__.py file:
1. It can be completely empty — just its presence used to be enough to mark the folder as a package.

2. When you have a folder full of .py files and you want to import from that folder like a module, Python needs a way to recognize it as a package (a collection of modules) rather than just an ordinary directory. Historically (and still commonly), that's what __init__.py does.

Example structure
myproject/
│
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module1.py
    └── module2.py
    
Because mypackage/ contains an __init__.py, you can now do this from main.py:

from mypackage import module1
from mypackage.module2 import some_function

Without __init__.py (in older Python versions especially), Python wouldn't treat mypackage as something you can import from.

What goes inside __init__.py
It can be completely empty — just its presence used to be enough to mark the folder as a package.
But it can also be used to:

1. Run setup code when the package is imported
python# mypackage/__init__.py
print("mypackage is being loaded")

2. Control what gets exposed when someone does from mypackage import *
python# mypackage/__init__.py
__all__ = ['module1', 'module2']

3. Make imports shorter/cleaner for users of your package

Instead of forcing users to write:
from mypackage.module1 import some_function

You can put this inside __init__.py:
python# mypackage/__init__.py
from .module1 import some_function

Now users can just write:
from mypackage import some_function
"""

"""
Traceback :
is a python module that provides a standard interface to extract, format and print stack traces of a python program. 
When it prints the stack trace it exactly mimics the behaviour of a python interpreter.

# importing module
import traceback
# declaring array
A = [1, 2, 3, 4]
try:
    value = A[5]
except:
    # printing stack trace
    traceback.print_exc()
# out of try-except
# this statement is to show that the program continues 
# normally after the exception is handled
print("end of program")
"""
