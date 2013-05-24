# Veronika Klantsak Als-11

# Write a function subsumes() that holds of two feature structures fs1 and fs2
# just in case fs1 subsumes fs2

import nltk
fs1 = nltk.FeatStruct("[E = [C = c]]")
fs2 = nltk.FeatStruct("[E = [C = c], B = [D = [C = c]]]")
# subsume our feature structures If fs1 subsumes fs2 ,then fs2 must have all the paths and path equivalences
# of fs1, and may have additional paths and equivalences as well
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