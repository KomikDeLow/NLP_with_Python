# Valerii Androshchuk APL(s)-13.
# Chapter 9, Task 9.
# List two feature structures that subsame [A=?x, B=?x].

import nltk
feature_structure1=nltk.FeatStruct("[A= ?x, B= ?x]")
feature_structure2 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
feature_structure1.unify(feature_structure2)
#Two features subsamed.
feature_structure1=nltk.FeatStruct("[A= ?x, B= ?x]")
feature_structure2 = nltk.FeatStruct("[B=k]")
feature_structure1.unify(feature_structure2)
result=feature_structure1.unify(feature_structure2)
print result
#Result displayed
