# Presented by Iuliia Tsymbalista ALs-13
# chapter 9, ex. 9

#List two feature structures that subsume [A=?x, B=?x].



import nltk

#giving values to features:
#example 1:

fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[B = [D = [C=E]]]")
print 'example 1'
print fs1.unify(fs2)

#example 2:

fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("""[A = D,
                           E = [ C = 74,
                           F = 'true']]""")
print 'example 2'
print fs1.unify(fs2)


#example 3:
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[A = ?x, B = 2, C=?x]")
print 'example 3'
print fs1.unify(fs2)
