# Presented by Olha Truniak, Chapter 9, Ex. 9
# List two feature structures that subsume [A=?x, B=?x].


import nltk
# Exploring feature structures (fs1 and fs8)
fs1=nltk.FeatStruct("[A= ?x, B= ?x]")
fs8 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
fs1.unify(fs8) # Subsume two feature structures
fs1=nltk.FeatStruct("[A= ?x, B= ?x]")
fs8 = nltk.FeatStruct("[B=k]")
fs1.unify(fs8)
print fs1.unify(fs8)
