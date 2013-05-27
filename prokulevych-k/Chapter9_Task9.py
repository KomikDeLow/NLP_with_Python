# fine

#Прокулевич К. ПРЛс-11, Розділ9, Задача 9
#List two feature structures that subsume [A=?x, B=?x].
import nltk
#giving values to features:
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[B = D]")
print fs1.unify(fs2)
fs1 = nltk.FeatStruct ("[A = ?x, B = ?x]")
fs2 = nltk.FeatStruct ("[A = [ B= d]]")
print fs1.unify(fs2)
