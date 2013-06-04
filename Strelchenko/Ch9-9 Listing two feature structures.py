import  nltk
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]") # asssigning  values to features
fs2 = nltk.FeatStruct ("[B = [C = d]]")    
print fs1.unify(fs2)  
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[A = s]")
print fs1.unify(fs2)   # merging information from two feature structures and outputing it
