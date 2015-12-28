def liz(s, l):
    while not l.empty() and not s.empty():
        if len(s) != len(l):
            return False
        else:
            if l[0] = s[0]:
                for item in l:
                    if l[item] != s[item]:
                        return False
                    else:
                        return True
                        
    
liz(s, l)