# List two feature structures that subsume [A=?x, B=?x].

import nltk
#giving values to features
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[B = [D = [C=E]]]")
print 'example 1'
print fs1.unify(fs2)
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("""[A = D,
E = [ C = 74,
F = 'true']]""")
print 'example 2'
print fs1.unify(fs2)
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[A = ?x, B = 2, C=?x]")
print 'example 3'
print fs1.unify(fs2)
