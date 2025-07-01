from random import *
import os
from datetime import *


def open_file():
    file = input("File: ")
    arch = open(file, 'r')
    readable = arch.read()
    print(readable)



print("Welcome to the open file system from Python")
route = os.getcwd()
date = datetime.today()
print(f"Your route is {route}")
try:
    open_file()
except:
    print("FailedNotFound")
else:
    print("Succesfull process")
finally:
    print("End of the Process")



