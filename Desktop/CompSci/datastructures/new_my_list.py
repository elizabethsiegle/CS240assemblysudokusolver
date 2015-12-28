"""
Lizzie Siegle
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
>>> print (my_list().prepend(2)).__eq__(my_list().prepend(4))
False
>>> print (my_list().prepend(2).prepend(4).prepend(10)).__eq__(my_list().prepend(2).prepend(4).prepend(10))
True
>>> print (my_list()).__eq__(my_list())
True
>>> print my_list().prepend(2).prepend(4).prepend(10).index(2)
2
>>> print my_list().prepend(2).prepend(4).index(0)
4
>>> print my_list().prepend(2).prepend(4).prepend(6).prepend(8).prepend(10).remove(4)
[10, 8, 6, 4]
>>> print my_list().prepend(2).prepend(3).remove(0)
[2]
>>> sample = my_list().prepend(5).prepend(3).prepend(16)
>>> print sample
[16, 3, 5]
>>> print sample.remove(1)
[16, 5]

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
    #axiom: adds x to the front of list
    # Complexity: constant
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
    # Complexity: constant
    def empty(self):
        if self.rep == []:
            return True
        else:
            return False
   

    #   head(my_list())        === undefined (precondition out)
    #   head(my_list(h, r))    === h
    # Complexity: constant
    def head(self):
    	# REPLACE WITH YOUR CODE HERE
    	precondition(not self.empty())
    	return self.rep[0]
        

    #   rest(my_list())        === undefined (precondition out)
    #   rest(my_list(h, r))    === r
    # Complexity: constant
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
    #eq(my_list()) checks to see if lists are equal, sharing elements
    # Complexity: linear because searching/checking??
    def __eq__(self, other):
        # REPLACE WITH YOUR CODE HERE
        if self.rep == other.rep:
            return True
        else:
            return False
        	
    # display (just uses built-in python operation)
    # Complexity: constant
    def __str__(self):
        return str(self.rep)

    # abstraction (just uses built-in python operation)
    # Complexity: constant
    def __repr__(self):
        return repr(self.rep)

    # size
    # AXIOMS HERE
    #my_list(a, b, c)
    #size(my_list) === 3
    #returns length of list
    def size(self):
        # REPLACE WITH YOUR CODE HERE
        return len(self.rep)
    
    #Axioms for index(self, where):
        # index(my_list(), where) === undefined
#         index(my_list(h, r), where)
# 	    === undefined		if (where < 0) or (where is not an integer)
# 	    === h				if (where == 0)
# 	    === index(r, where-1)		else
#complexity: constant
    def index(self, where): #returns item at position where
        precondition(not self.empty())
        precondition(where >= 0)
        precondition(where < self.size())
        # for i in range(0, my_list()):
        if where == 0:
            return self.head() #0
        else:
            return self.rest().index(where -1)
        

 	    
    def remove(self, where):
        precondition(not self.empty())
        precondition(where >= 0)
	# mutate the list such that the item in original position
        # where is no longer in list
        #complexity: linear
    
        if where == 0:
            return self.rep[1:]
        elif where == self.size() -1:
            return self.rep[:self.rep[where-1]]
        elif where >= self.size():
            return None
        else:
            return self.rep[:where] + self.rep[where+1:] #up to but not including where

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"
