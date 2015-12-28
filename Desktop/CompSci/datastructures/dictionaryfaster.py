"""
  Dictionary class, and two implementations

>>> d = Dictionary1faster()
>>> d.put('Dave', 4973)
>>> d.put('J.D.', 4993)
>>> d.put('CS lab', 1202)
>>> d.lookup('Dave')
1
>>> print d
{'CS lab': 1202, 'Dave': 4973, 'J.D.': 4993}

>>> d.lookup('CS lab')
0

>>> d.lookup('Steven')
'No entry'

>>> d.put('Steven', 1203)
>>> d.lookup('Steven')
3

>>> d2 = Dictionary1faster()
>>> d.__eq__(d2)
False

# Add some tests of "merge" here
>>> d4 = Dictionary1faster()
>>> d4.put('Lizzie', 2424)
>>> d4.put('Tommy', 2468)
>>> d4.put('Rachel', 1359)
>>> d5 = Dictionary1faster()
>>> d5.put('Federer', 1234)
>>> d5.put('Lincecum', 1818)
>>> d5.put('Durant', 9876)
>>> d4.mergeSort(d5)
{'Durant': 9876, 'Federer': 1234, 'Lincecum': 1818, 'Lizzie': 2424, 'Rachel': 1359, 'Tommy': 2468}
>>> d6 = Dictionary1faster()
>>> d6.put('Katherine', 2468)
>>> d6.put('Rachel', 1359)
>>> d4.mergeSort(d6)
error
>>> d5 = Dictionary1faster()
>>> d7 = Dictionary1faster()
>>> d5.mergeSort(d7) #empty merge with empty
[]
>>> d5.mergeSort(d4) #empty dictionary merge with nonempty
{'Lizzie': 2424, 'Rachel': 1359, 'Tommy': 2468}
>>> d7.put('Lizzie', 2424)
>>> d7.put('Tommy', 2468)
>>> d7.put('Rachel', 1359)
>>> print d7
{'Lizzie': 2424, 'Rachel': 1359, 'Tommy': 2468}
>>> print d4
{'Lizzie': 2424, 'Rachel': 1359, 'Tommy': 2468}

>>> d4.__rep_inv__()
True

>>> d100 = Dictionary1faster()
>>> d100.put('Teresa', 3)
>>> d100.put('Savannah', 2)
>>> d100.put('Lea', 1)
>>> d100.__rep_inv__()
True
"""
# make Python look in the right place for logic.py, or complain if it doesn't
from __builtin__ import True
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)



class Dictionary1faster:
    """
        A dictionary represented with a Python list.
        Each list element is a tuple of two parts, the key and the value
    """
    def __init__(self):
        precondition(True)
        self.__listOfPairs = []
        self.__listOfKeys = []
        self.__listOfValues = []

    # "extending" constructor method: 'with'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
    def withEntry(self, key, value):
        precondition(True)
        result = Dictionary1faster()
        result.__listOfPairs = [ (key, value) ] + self.__listOfPairs
        return result
    
    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #or d.lookup(x), otherwise
    def lookup(alist, item): #binary search
        precondition(True)
        first = 0
        last = len(alist.__listOfPairs)-1
        found = False
        while first<=last and not found:
            midpoint = (first + last)/2
            if alist.__listOfPairs[midpoint] == item:
                found = True
                return midpoint
            else:
                if item < alist.__listOfPairs[midpoint]:
                    last = midpoint-1
                    return last
                else:
                    first = midpoint+1
                    return first
        return found
    
    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    def put(self, key, value):
        precondition(True)
        self.__listOfPairs = [ (key, value) ] + self.__listOfPairs
        self.__listOfKeys.append(key)
        self.__listOfPairs = sorted(self.__listOfPairs)
        self.__listOfKeys = sorted(self.__listOfKeys)
        
    #complexity: linear because you must search lists
    def __eq__(self,otherDictionary):
        precondition(isinstance(otherDictionary,Dictionary1faster) )
        "replace this with your equality test"
        if self.__listOfPairs == otherDictionary.__listOfPairs:
            return True
        else:
            return False
    
    def remove(self, where):
        if where == 0:
            return self.__listOfPairs[1:]
        elif where == len(self.__listOfPairs) -1:
            return self.__listOfPairs[:self.__listOfPairs[where-1]]
        elif where >= len(self.__listOfPairs):
            return None
        else:
            return self.__listOfPairs[:where] + self.__listOfPairs[where+1:] #up to but not including where

    # axioms: both d, d1 {} -> d.merge(d1) returns empty dictionary, none
    #d = {}, d1 !empty -> d.merge(d1) would return d1+d (d1)
    #both have items -> d.merge(d1) would return all items of d, d1
    #duplicate keys -> d.merge(d1) would return 'error' message
    #  fill these in
    #complexity: 
    def mergeSort(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1faster) )
        "replace this with a function to merge two dictionaries and return a composite"
        for key, value in self.__listOfPairs:
            self.__listOfKeys.append(key)
            self.__listOfValues.append(value)
        if sorted(self.__listOfKeys) == sorted(otherDictionary.__listOfKeys) and sorted(self.__listOfValues) == sorted(otherDictionary.__listOfValues):
            sort = True
        else:
            sort = False
    
        #if dictionaries are both the same
        if self.__listOfPairs == otherDictionary.__listOfPairs:
            return otherDictionary.__listOfPairs 

        #if dictionaries are both empty
        if self.__listOfPairs == {}:
            empty = True
            if empty:
                return {}
        same_keys = False
        for value1 in self.__listOfPairs:
            for value2 in otherDictionary.__listOfPairs:
                #if values are the same/duplicates, same_keys = True, so can't merge
                if value1[0] == value2[0]:
                    same_keys = True
                    #remove(self.__listOfPairs, value1[0])
                    print 'error'
        #if not same, create new dictionary and add to it
        if same_keys == False:
            new_dict = Dictionary1faster()
            new_dict.__listOfPairs = self.__listOfPairs + otherDictionary.__listOfPairs
            new_dict.__listOfPairs = sorted(new_dict.__listOfPairs)
            return new_dict
        
    def __rep_inv__(self):  
        if self.__listOfPairs == sorted(self.__listOfPairs):
            return True
        else:
            return False 
        
    def __repr__(self):
        precondition(True)
        string_bracket = '{'
        for i in range(len(self.__listOfPairs)):
#             if __rep_inv(self.__listOfPairs[i]) == False:
#                 self.__listOfPairs = sorted(self.__listOfPairs)
            #last item, end with }
            if i == len(self.__listOfPairs)-1:
                string_bracket = string_bracket + "%s: %s}" %(repr(self.__listOfPairs[i][0]), repr(self.__listOfPairs[i][1]))
            #connect different keys and values with comma
            else:
                string_bracket = string_bracket + "%s: %s, " % (repr(self.__listOfPairs[i][0]), repr(self.__listOfPairs[i][1]))
        return string_bracket

class Dictionary2:
    """
        A dictionary represented with a binary tree
    """
    def __init__(self):
        precondition(True)
 
    # "extending" constructor method: 'withEntry'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
    def withEntry(self, key, value):
        precondition(True)
 
 
    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
 
 
    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    def put(self, key, value):
        precondition(True)
 
    def __eq__(self,otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1) )
 
    # axioms:
    #  fill these in
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1faster) )
         
    def __repr__(self):
        precondition(True)

# by default, use the first representation, but this is changed in DocTest below
Dictionary = Dictionary1faster

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Dictionary
    whatever_dictionary_was = Dictionary

    print "=========================== Running doctest tests for Dictionary1 ===========================\n"
    Dictionary = Dictionary1faster
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"

    print "\n\n\n\n"
    print "=========================== Running doctest tests for Dictionary2 ===========================\n"
    Dictionary = Dictionary2
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"
    Dictionary = whatever_dictionary_was

if __name__ == "__main__":
    _test()
