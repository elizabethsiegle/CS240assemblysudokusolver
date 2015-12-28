"""
Tradeoffs of using a binary tree to represent a dictionary compared to using a list:
a binary search tree is sorted already, so it's faster to find something whereas a list is 
unsorted, so it takes longer to find something. At the same time, because of that, it is faster
to insert something into a list and takes longer to insert something into a binary search tree.
So a binary search tree is also faster compared to a binary tree to find something, and slower
to insert something.
A binary search on an sorted list would be similar to a search on a binary search tree.
Dictionary class, and two implementations

**Please excuse this lab I know it's not right I just honestly gave up and decided my time would 
better be spent studying for the Discrete test Thursday because I'd be busy all day Wednesday with
an away tennis match and I was going to ask for an extension but we already got one and I went to TA
hours at night but just ugh __repr__ and merge... and I know it's no excuse but it is a reason**
>>> d = Dictionary2()
>>> d.put('Dave', 4973)
>>> d.put('J.D.', 4993)
>>> d.put('CS lab', 1202)
>>> d.lookup('Dave')
4973

>>> d.put('Dave', 1202)  # when Dave is working in the lab

>>> d.lookup('Steven')
'No entry'

>>> d2 = d.withEntry('Steven', 1203)
>>> d.lookup('Steven')
'No entry'

>>> d2.lookup('Steven')
1203

>>> d == d2
False

# Add some tests of "merge" here
>>> d4 = Dictionary2()
>>> d4.put('Lizzie', 2424)
>>> d4.put('Rachel', 1359)
>>> d4.put('Tommy', 2468)
>>> print d4
{'Lizzie':2424, 'Rachel':1359, 'Tommy':2468}
>>> d5 = Dictionary2()
>>> d5.put('Federer', 1234)
>>> d5.put('Lincecum', 1818)
>>> d5.put('Durant', 9876)
>>> d4.merge(d5)
{'Lizzie':2424, 'Rachel':1359, 'Tommy':2468, 'Durant':9876, 'Federer':1234, 'Lincecum':1818}
>>> d5 = Dictionary2()
>>> d7 = Dictionary2()
>>> d5.merge(d7) #empty merge with empty
[]
>>> d5.merge(d4) #empty dictionary merge with nonempty
{Lizzie':2424, 'Rachel':1359, 'Tommy':2468}
>>> d7.put('Klee', 2)
>>> d7.put('Rxu', 1)
>>> d7.put('Lsiegle', 8)
>>> print d7
{'Klee':2, 'Lsiegle':8, 'Rxu':1}

"""
# make Python look in the right place for logic.py, or complain if it doesn't
from __builtin__ import True
from gi.overrides.keysyms import Left
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)



# class Dictionary1:
#     """
#         A dictionary represented with a Python list.
#         Each list element is a tuple of two parts, the key and the value
#     """
#     def __init__(self):
#         precondition(True)
#         self.__listOfPairs = []
# 
#     # "extending" constructor method: 'with'
#     #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
#     def withEntry(self, key, value):
#         precondition(True)
#         result = Dictionary1()
#         result.__listOfPairs = [ (key, value) ] + self.__listOfPairs
#         return result
#     
#     # axioms:
#     #  Dictionary().lookup(x) === "No entry"
#     #  d.withEntry(k, v).lookup(x) === v, if k==x
#     #or d.lookup(x), otherwise
#     def lookup(self, key): 
#         precondition(True)
#         for pair in self.__listOfPairs:
#             if pair[0] == key:
#                 return pair[1]
#         return False
# 
#     # axioms: 
#     #  d.put(k, v) --> new d is d.withEntry(k, v)
#     def put(self, key, value):
#         precondition(True)
#         self.__listOfPairs = [ (key, value) ] + self.__listOfPairs
# 
#     #complexity: linear because you must search lists
#     def __eq__(self,otherDictionary):
#         precondition(isinstance(otherDictionary,Dictionary1) )
#         "replace this with your equality test"
#         if self.__listOfPairs == otherDictionary.__listOfPairs:
#             return True
#         else:
#             return False
#     
#     def remove(self, where):
#         if where == 0:
#             return self.__listOfPairs[1:]
#         elif where == len(self.__listOfPairs) -1:
#             return self.__listOfPairs[:self.__listOfPairs[where-1]]
#         elif where >= len(self.__listOfPairs):
#             return None
#         else:
#             return self.__listOfPairs[:where] + self.__listOfPairs[where+1:] #up to but not including where
# 
#     # axioms: both d, d1 {} -> d.merge(d1) returns empty dictionary, none
#     #d = {}, d1 !empty -> d.merge(d1) would return d1+d (d1)
#     #both have items -> d.merge(d1) would return all items of d, d1
#     #duplicate keys -> d.merge(d1) would return 'error' message
#     #  fill these in
#     #complexity: O(n**2)
#     def merge(self, otherDictionary):
#         precondition( isinstance(otherDictionary,Dictionary1) )
#         "replace this with a function to merge two dictionaries and return a composite"
#         #if dictionaries are both the same
#         if self.__listOfPairs == otherDictionary.__listOfPairs:
#             return otherDictionary.__listOfPairs 
# 
#         #if dictionaries are both empty
#         if self.__listOfPairs == {}:
#             empty = True
#             if empty:
#                 return {}
#         same_keys = False
#         for value1 in self.__listOfPairs:
#             for value2 in otherDictionary.__listOfPairs:
#                 #if values are the same/duplicates, same_keys = True, so can't merge
#                 if value1[0] == value2[0]:
#                     same_keys = True
#                     #remove(self.__listOfPairs, value1[0])
#                     print 'error'
#         #if not same, create new dictionary and add to it
#         if same_keys == False:
#             new_dict = Dictionary1()
#             new_dict.__listOfPairs = self.__listOfPairs + otherDictionary.__listOfPairs
#             return new_dict
#         
#     #complexity: O(n)
#     def __repr__(self):
#         precondition(True)
#         #assert(Dictionary == sorted(Dictionary))
#         string_bracket = '{'
#         for i in range(len(self.__listOfPairs)):
#             #last item, end with }
#             if i == len(self.__listOfPairs)-1:
#                 string_bracket = string_bracket + "%s: %s }" %(repr(self.__listOfPairs[i][0]), repr(self.__listOfPairs[i][1]))
#             #connect different keys and values with comma
#             else:
#                 string_bracket = string_bracket + "%s: %s, " % (repr(self.__listOfPairs[i][0]), repr(self.__listOfPairs[i][1]))
#         return string_bracket
# #         for k in range(len(self.__listOfPairs)):
# #             if not __rep_inv__(self.__listOfPairs[k]): 
# #                  self.__listOfPairs = sorted(self.__listOfPairs)
# #             else:
# #                 print "%s, %s" % (k, self.listOfPairs[k]) 

class node:
    def __init__(self, key, val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    def has_leftchild(self):
        return self.leftChild
    
    def has_rightchild(self):
        return self.rightChild
    
    def __repr__(self):
        node_rep =  str(self.key) + "," + " " + str(self.val)
        return node_rep

#from copy import deepcopy #unneeded?? make deepcopy for withEntry() method
class Dictionary2:
    """
        a binary search tree representation
    """
    
    def __init__(self, r_key=None, r_val = None, left = None, right = None):
        if r_key == None:
            self.root = None
            self.r_key = None
            self.r_val = None
        else:
            self.r_key = r_key
            self.r_val = r_val
            self.root = node(r_key, r_val, left, right, parent = None)
            
    def right(self):
        precondition(not self.empty())
        return self.root.rightChild
    
    def left(self):
        precondition(not self.empty())
        return self.root.leftChild
 
    def __rep_inv__(self):
        if not self.root: #can't be == 0 because 0 != None, declared as None
            return True
        elif self.root.leftChild == None and self.root.rightChild == None: 
            #no clue why this works (doesn't return error), like self.left(), and other variations
            return True
        else:
            if self.left():  #does it exist? if so...
                if self.left().key < self.root.key:
                    return True 
                    # return self.left().__rep_inv__() #necessary?? needed?
                else:
                    return False
            if self.right(): #does self.root.rightChild exist??...
                if self.right().key > self.root.key:
                    return True 
                    #return self.right().__rep_inv__() 
                else:
                    return False
        
    def empty(self):
        return self.root == None
    
    def size(self):
        if self.empty(): #recursion
            return 0
        else:
            return self.left().size() + self.right().size()
        
    # "extending" constructor method: 'withEntry'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
    def withEntry(self, r_key, r_value):
        precondition(True)
        result = Dictionary2()
        result.put(r_key, r_value)
        return result
    # axioms: complexity: O(lg(n))
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
        if self.root:
            yes = self._get(key, self.root)
            if yes:
                return yes.val
            else:
                return 'No entry'
        else:
            return 'No entry'
        
    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)
        
    def put(self, key, value):
        if self.root:
            self.__put(key, value, self.root)
        else:
            self.root = node(key, value)
    
    
    # axioms: helper method
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    def __put(self, key, value, present_node): #= none):
        precondition(True)
        if key < present_node.key:
            if present_node.has_leftchild(): #node has leftchild, not left() 
                self.__put(key, value, present_node.leftChild)
            else:
                present_node.leftChild = node(key, value, parent=present_node)
        else:
            if present_node.has_rightchild():
                self.__put(key, value, present_node.rightChild)
            else:
                present_node.rightChild = node(key, value, parent = present_node)
   
    #complexity: O(log(n))
    def __eq__(self,otherDictionary):
        precondition(isinstance(otherDictionary,Dictionary2) )
        return self.__repr__() == otherDictionary.__repr__()
    
    # axioms: complexity: O(n(log(n)))
    #  fill these in
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2) )
        #if both empty
        if self.empty() and otherDictionary.empty():
            return []
        elif self.empty() and not otherDictionary.empty():
            return otherDictionary
        elif otherDictionary.empty():
            return self
        else:
            if otherDictionary.left() != otherDictionary.left().empty():
                if otherDictionary.right() != otherDictionary.right().empty():
                    self.put(otherDictionary.root, otherDictionary.root)
                    self.merge(otherDictionary.left())
                    self.merge(otherDictionary.right())
        return self
        # elif self.empty() and otherDictionary.root:
        #     return str(otherDictionary.root) + str(otherDictionary.right()) + str(otherDictionary.left()) #don't know why Tommy isn't being returned
#         elif otherDictionary.empty() and self.root:
#             return "{" + str(self.r_key) + str(self.right().r_key) + str(self.right().r_val) + str(self.left().r_key) + str(self.left().r_val) #str(self.left()) + str(self.right())
#         elif otherDictionary.root or self.root:
#             #if 1 empty
#             if self.empty() and otherDictionary.root >= 1:
#                 return str(otherDictionary.root) + str(otherDictionary.left().r_key) + str(otherDictionary.left().r_val) + str(otherDictionary.right().r_key) + str(otherDictionary.right().r_val)
#             elif otherDictionary.empty() and self.root >= 1:
#                 return str(self.root) + str(self.left().r_key)+str(self.left().r_val) + str(self.right().r_key) + str(self.right().r_val)
#             else: #both are not empty
#                 return str(self.root) + str(self.left()) + str(self.right()) + str(otherDictionary.root) + str(otherDictionary.left()) + str(otherDictionary.right())
        assert(self.__rep_inv__()) #difference between assert and self.__rep_inv__() ??
        postcondition(self.__rep_inv__())

    def __repr__(self): 
        l = "{"
        if self.empty(): #if empty. base case
            return "{}"
        else:
            if self.root != None: #self.root exists
                l += "'" + str(self.root.key) + "'" + ":" + str(self.root.val) + "'" 
                if self.root != self.right():
                    l+= str(self.right()) #"'" + str(self.right().r_key) +"'"+":" + str(self.right().r_val) 
                elif self.root != self.left():
                    l+= "'"+str(self.left().r_key)+"'"+":"+str(self.left().r_val) #str(self.left().r_key, r_val return attribute error. why?? when self.right().r_key passes
               
                postcondition(self.__rep_inv__())
            while self.left(): #as long as self.left() isn't empty keep going
                l += self.left().__repr__() 
                break
            while self.right(): 
                l += ","  + self.right().__repr__()
                break
        postcondition(self.__rep_inv__())
        return l + "}"
        
            #return '<BST: (%s)>' % ', '.join('%r' % v for v in self)
# by default, use the first representation, but this is changed in DocTest below
Dictionary = Dictionary2()

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Dictionary
    whatever_dictionary_was = Dictionary

#     print "=========================== Running doctest tests for Dictionary1 ===========================\n"
#     Dictionary = Dictionary2
#     result = doctest.testmod()
#     if result[0] == 0:
#         print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
#     else:
#         print "Rats!"

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