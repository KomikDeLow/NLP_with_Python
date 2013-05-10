# fine

#Presented by Tetiana Kobryn

#Chapter 9 Ex.8
#Consider the feature structures shown in Example 9-5. Work out on paper
#what the result is of the following unifications. (Hint: you might
#find it useful to draw the graph structures.)

import nltk
#defining feature structures
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
#unifying different feature structures
a = fs1.unify(fs2)
b = fs1.unify(fs3)
c = fs4.unify(fs5)
d = fs5.unify(fs6)
e = fs5.unify(fs7)
f = fs8.unify(fs9)
g = fs8.unify(fs10)

print "a"
print a
print "b"
print b
print "c"
print c
print "d"
print d
print "e"
print e
print "f"
print f
print "g"
print g
