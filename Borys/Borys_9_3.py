# Roman Borys PRLs-11
import nltk
#defining subs function
def subs(fs1, fs2):
        if fs1.subsumes(fs2):
                return fs1.unify(fs2)
        elif  fs2.subsumes(fs1):
                return fs2.unify(fs1)
        else:
                return "this structures don't subsume each other"

# showing functions results 
print """ input data 1:
                fs1 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
                fs2 = nltk.FeatStruct("[B = [D = d]]")
 result:"""
fs1 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
fs2 = nltk.FeatStruct("[B = [D = d]]")
print subs(fs1, fs2)
print
print """ input data 2:
                fs1 = nltk.FeatStruct("[A = [D = d]]")
                fs2 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
 result:"""
fs1 = nltk.FeatStruct("[A = [D = d]]")
fs2 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
print subs(fs1, fs2)
