"""
my_list class:
    A simple list class with operations that can be performed quickly.
    By John Dougherty, possibly Kris Brower, Dave Wonnacott

Examples:
>>> print my_list()
[]
>>> print my_list().prepend(5)
[5]
>>> print my_list().prepend(5).prepend(3).prepend(16)
[16, 3, 5]

>>> print my_list().empty()
True
>>> print my_list().prepend(5).prepend(3).prepend(16).empty()
False

>>> print my_list().prepend(5).prepend(3).prepend(16).head()
16
>>> print my_list().prepend(5).prepend(3).prepend(16).rest()
[3, 5]
>>> print my_list().prepend(5).prepend(3).prepend(16).rest().head()
3
>>> print my_list().prepend(5).prepend(3).prepend(16).size()
3
>>> print my_list().prepend(5).prepend(3).prepend(16).rest().size()
2
"""
import sys
sys.path.append('/home/courses/python')
from logic import *


class my_list:

    # First, the constructors:
    #  A list is either empty, or an item followed by a list 

    # constructor: primitive (my_list())
    # Complexity: 
    def __init__(self):
        self.rep = []

    # constructor: prepending (my_list(l, x))
    # precondition: self must be a my_list (this has to be true in Python)
    # Complexity: 
    def prepend(self, x):
        t = my_list()
        t.rep = [x] + self.rep
        return t

    # Now the accessor functions:
    #  empty, head, rest, and equality checking
    #  Also, for convenience, a printing function

    #empty
    #axioms: 
    #   empty(my_list())        === True
    #   empty(my_list(h, r))    === False
    # Complexity: 
    def empty(self):
        if self.rep == []:
        	return True
        else:
        	return False
   

    #   head(my_list())        === undefined (precondition out)
    #   head(my_list(h, r))    === h
    # Complexity: 
    def head(self):
    	# REPLACE WITH YOUR CODE HERE
    	precondition(not self.empty())
    	h= my_list()
    	h.rep = self.rep[-1]
    	return h
        

    #   rest(my_list())        === undefined (precondition out)
    #   rest(my_list(h, r))    === r
    # Complexity: 
    def rest(self):
        precondition(not self.empty())
        r = my_list()
        r.rep = self.rep[1:]
        return r

    # equals
    # AXIOMS HERE: my_list(a, b, c) 
    #other_list(a, b, c)
    #my_list.eq(other)  === True
   	#my_list.append(d)
   	#my_list.eq(other) === False
    #eq(my_list()
    # Complexity: 
    def __eq__(self, other):
        # REPLACE WITH YOUR CODE HERE
        precondition(not self.empty())
        o=other.rep()
        if len(self) == len(other):
        	for i in my_list():
        		for o in o:
        			if my_list[i] == o[-o]:
        				return True
        			else:
        				return False
        		
        	
    # display (just uses built-in python operation)
    # Complexity: 
    def __str__(self):
        return str(self.rep)

    # abstraction (just uses built-in python operation)
    # Complexity: 
    def __repr__(self):
        return repr(self.rep)

    # size
    # AXIOMS HERE
    #my_list(a, b, c)
    #	size(my_list) === 3
    def size(self):
        # REPLACE WITH YOUR CODE HERE
		return len(self)

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"

        """
Determine whether or not a list is a "palindrome"

Examples:
>>> print palindrome(my_list().prepend(5).prepend(3).prepend(16))
False
>>> print palindrome(my_list().prepend(16).prepend(3).prepend(16))
True

"""
# import sys
# sys.path.append('/home/courses/python')
# from logic import *
# from my_list import *
# 
# 
# def palindrome(l):
#     """replace this with your "palindrome" function """
# 	new_l= str(l)
# 	for item in l:
# 		if l[item] == l[-1]:
# 			-1 -= 1
# 			
# 
# # The following gets the "doctest" system to check test cases in the documentation comments
# 
# def _test():
#     import doctest
#     return doctest.testmod()
# 
# if __name__ == "__main__":
#     if _test()[0] == 0:
#         print "Congratulations! You have passed all the tests"
