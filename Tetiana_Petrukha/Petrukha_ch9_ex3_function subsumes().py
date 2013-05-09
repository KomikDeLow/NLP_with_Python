# Petrukha Tetiana Als-11
# Chapter_9, Ex_3

# Write a function subsumes() that holds of two feature structures fs1 and fs2
# just in case fs1 subsumes fs2

import nltk
fs1 = nltk.FeatStruct("[B = [C = ?x]]")
fs2 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
print fs1.subsumes (fs2) # checks whether fs1 subsumed in fs2
print fs2.subsumes (fs1) # checks whether fs2 subsumed in fs1

# This function unify two feature structures fs1 and fs2 in case if fs1 subsumes fs2
def subs (fs1, fs2):
    if fs1.subsumes (fs2):
        print fs1.unify(fs2)
    elif fs2.subsumes (fs1):
        print fs2.unify(fs1)
    else: print "None"


print subs(fs1,fs2)

    
