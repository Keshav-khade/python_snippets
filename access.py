from mypackage1.prg1 import show
from mypackage1.prg2 import display
from mypackage2.prg1 import testing
from mypackage1.subpackage.prg3 import f1
# examples of private packages
"""
# working with module alias

import mypackage1.prg1 as p1
import mypackage1.prg2 as p2
import mypackage1.subpackage.prg3 as p3
import mypackage2.prg1 as m1

print("from accessing module")

p1.show()
p2.display()
p3.f1()
m1.testing()

print("End of main module")
"""

"""
# packages with their modules and we have to import them using their names only
import mypackage1.prg1
import mypackage1.prg2
import mypackage1.subpackage.prg3
import mypackage2.prg1

print("from accessing module")

mypackage1.prg1.show()
mypackage1.prg2.display()
mypackage1.subpackage.prg3.f1()
mypackage2.prg1.testing()

print("End of main module")
"""

"""
from mypackage1.prg1 import show
from mypackage1.prg2 import display
from mypackage2.prg1 import testing
from mypackage1.subpackage.prg3 import f1

# accessing packages without package and module names
show()
display()
testing()
f1()
"""
# accessing packages without package and module names
show()
display()
testing()
f1()

"""
import sys
print(sys.executable)
"""

"""
import sys

for path in sys.path:
   print(path)
"""
# import sys
# print(sys.executable)
# print(sys.path)