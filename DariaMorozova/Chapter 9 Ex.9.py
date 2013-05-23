# Daria Morozova
# Chapter 9 Ex.9


import nltk
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")  # giving values to features
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[B =[D=d]]")
print fs1.unify(fs2)

fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("""[A = C,
                           E = [ D = 74,
                           F = 'false']]""")
print fs1.unify(fs2)
