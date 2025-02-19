import china
from china import greet
import sys
import pandas
from senegal import greet

print("hello world")
china.cook() # function
china.greet()
greet() # no need for import china and then china.greet
print(china.hello) # string


# what if there is a collision in greets?

def greet():
    print("hellooooo")   # It overwrites the other function, since this was last
greet()


import china
from china import cook as china_cook, is_prime as prime
from sengal import cook as senegal_cook
try:
    from romania import cook as romania_cook
except ModuleNotFoundError:
    print("Sorry there is nocook in romania")

import sys
import pandas

print("hello world")
def greet():
    print("hello from segoland")

def cook():
    print("im making cochinillo")

cook()
senegal_cook()
china_cook()

prime(4)