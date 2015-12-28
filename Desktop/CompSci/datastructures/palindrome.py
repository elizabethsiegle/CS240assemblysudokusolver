"""
Determine whether or not a list is a "palindrome"

Examples:
>>> print palindrome(my_list().prepend(5).prepend(3).prepend(16))
False
>>> print palindrome(my_list().prepend(16).prepend(3).prepend(16))
True

"""
import sys
sys.path.append('/home/courses/python')
from logic import *
from my_list import *
from reverse import *


def palindrome(l):
    #palindrome(mylist().prepend(16).prepend(3).prepend(16) return true
    #checks to see if mylist() is a palindrome
    #complexity: linear ??
    """replace this with your "palindrome" function"""
    #return reverse(l)
    #precondition(isinstance(l, my_list))
    if l == reverse(l):
        return True
    else: 
        return False

    
    
    
'''print palindrome(my_list().prepend(16).prepend(3).prepend(16))
print palindrome(my_list().prepend(5).prepend(3).prepend(16))
both return False'''
# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"
