# Halyna Khimka
# Feature Structure Unifications
# Chapter 9.8
#
"""
This module contains different ways of unifying feature structures and its results.
The explanations of the results are below.
"""
import nltk

fs1 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
fs2 = nltk.FeatStruct("[B = [D = d]]")
fs3 = nltk.FeatStruct("[B = [C = d]]")
fs4 = nltk.FeatStruct("[A = (1)[B = b], C->(1)]")
fs5 = nltk.FeatStruct("[A = (1)[D = ?x], C = [E -> (1), F = ?x] ]")
fs6 = nltk.FeatStruct("[A = [D = d]]")
fs7 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
fs8 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
fs9 = nltk.FeatStruct("[A = [B = b], C = [E = [G = e]]]")
fs10 = nltk.FeatStruct("[A = (1)[B = b], C -> (1)]")

print 'fs1 and fs2:  With this unification A has the same feature and B gets one more feature: D ->d:'
print fs1.unify(fs2)
print
print 'fs1 and fs3:  With this unification feature C gets a new feature d. Ans feature A has the same value as C, that is why A gets value d also.'
print fs1.unify(fs3)
print
print 'fs4 and fs5: Values of feature A from fs4 and fs where unified and they both had a path 1). That is why Feature C which has values B - b is directed to A (1) and feature E with its D-?x is directed to A(1) also.'
print fs4.unify(fs5)
print
print 'fs5 and fs6: A-D-?x and E-D-?x and F-?x have identical values. In fs6 A-D-d has the same path as in fs, that is why ?x have got values d. '
print fs5.unify(fs6)
print
print'fs5 and fs7: this feature structures have different paths in C-F-D-d. That is why the unifying is impossible.'
print fs5.unify(fs7)
print
print 'fs8 and fs9: With with unifying E-G-e from fs9 has the same path as G=?x in fs 8 that is why all values ?x get value e.'
print fs8.unify(fs9)
print
print 'fs8 and fs10: B-?x from fs8 is unified with B-b from fs10 because of identical paths. that is why a value ?x gets b. '
print fs8.unify(fs10)
