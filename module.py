"""
1️⃣ Module
A module is simply a Python file (.py) containing functions, classes, or variables.
When imported, Python executes the file once and stores it in memory.


2️⃣ import module
import one
          Imports the whole module object.
          Access members using one.function() or one.variable.
          ✅ Clear and safe for large projects.

3️⃣ from module import name
from one import x
          Imports only specific names into current namespace.
          Shorter syntax, but can cause confusion in large projects.


4️⃣ from module import *
          Imports everything from the module.
          ❌ Not recommended in professional code due to namespace conflicts.


5️⃣ __name__ (Dunder Variable)
          __name__ is a special built-in variable automatically set by Python.
          It tells whether the file is run directly or imported.


6️⃣ if __name__ == "__main__":
          This block runs only when the file is executed directly, not when imported.
          Used for testing or running demo code inside modules.
          

7️⃣ Module Execution Rule
When a module is imported:
          Python executes the file once
          Function definitions are stored
          Functions run only when explicitly called


8️⃣ sys.modules
          Python keeps imported modules in a dictionary called sys.modules.
          If a module is already there, Python does not execute it again.


9️⃣ Import Happens Only Once
          Even if you write:
                    import one
                    import one
                    The file executes only once because Python reuses the cached module.


🔟 Module = Object in Memory
          After importing, a module becomes an object stored in memory.
          Changing one.x modifies the module object directly.


1️⃣1️⃣ Reassignment vs Mutation
Reassignment:
          x = 100
          Creates a new object and breaks connection.
Mutation:
          x.append(4)
          Modifies the existing object in memory.
1️⃣2️⃣ Immutable vs Mutable
          Immutable (int, str, tuple):
          Cannot change value; reassignment creates new object.
          
          Mutable (list, dict, set):
          Can modify object in place; changes reflect everywhere.
"""