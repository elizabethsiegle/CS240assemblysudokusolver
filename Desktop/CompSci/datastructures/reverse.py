"""
Reverse a simple list using just "empty", "head", and "rest" and other functions written here

Examples:

INCLUDE AT LEAST TWO TEST CASES FOR append(l, x)
>>> print append(my_list().prepend(5).prepend(3).prepend(16), 3)
[16, 3, 5, 3]
>>> print append(my_list().prepend(2).prepend(4).prepend(24).prepend(25), 2000)
[25, 24, 4, 2, 2000]
>>> print reverse(my_list())
[]
>>> print reverse(my_list().prepend(5))
[5]
>>> print reverse(my_list().prepend(5).prepend(3))
[5, 3]
>>> print reverse(my_list().prepend(5).prepend(3).prepend(16))
[5, 3, 16]
"""
import sys
sys.path.append('/home/courses/python')
from logic import *
from my_list import *


# append
# AXIOMS HERE
#returns a list with value x at the end of the list
#complexity: constant
def append(l, x):
    # precondition(.... no precondition?
    if l == my_list():
        return my_list().prepend(x)
    else:
        return append(l.rest(), x).prepend(l.head())
#axiom: reverses the order of a list
#complexity: linear 
def reverse(l):
    """ replace this with your "reverse" function """
    if l.size() <= 1:
        return l
    else: 
        return append(reverse(l.rest()), l.head())
    

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"
