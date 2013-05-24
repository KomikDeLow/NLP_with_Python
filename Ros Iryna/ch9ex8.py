# Iryna Ros, PRLs-11, chapter 9, exercise 8

import nltk
# Entering the feature structures
fs1 = nltk.FeatStruct("[K = ?z, D= [C = ?z]]")
fs2 = nltk.FeatStruct("[D = [L = d]]")
fs3 = nltk.FeatStruct("[D = [C = d]]")
fs4 = nltk.FeatStruct("[K = (1)[D = b], C->(1)]")
fs5 = nltk.FeatStruct("[K = (1)[L = ?z], C = [E -> (1), F = ?z] ]")
fs6 = nltk.FeatStruct("[K = [L = d]]") 
fs7 = nltk.FeatStruct("[K = [L = d], C = [F = [L = d]]]")
fs8 = nltk.FeatStruct("[K = (1)[L = ?z, G = ?z], C = [D = ?z, E -> (1)] ]")
fs9 = nltk.FeatStruct("[K = [D = b], C = [E = [G = e]]]")
fs10 = nltk.FeatStruct("[K = (1)[D = b], C -> (1)]")
# Checking the results of the feature structures unifications with nltk
print 'Unification of the 1st and 2d feature structure:', fs1.unify(fs2)
print 'Unification of the 1st and 3d feature structure:', fs1.unify(fs3)
print 'Unification of the 4th and 5th feature structure:', fs4.unify(fs5)
print 'Unification of the 5th and 6th feature structure:', fs5.unify(fs6)
print 'Unification of the 5th and 7th feature structure:', fs5.unify(fs7)# These two feature structures won't unify
print 'Unification of the 8th and 9th feature structure:', fs8.unify(fs9)
print 'Unification of the 8th and 10th feature structure:', fs8.unify(fs10)
