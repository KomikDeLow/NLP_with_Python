# Chapter_9_Ex_9_Fursachyk
import nltk  
fs1=nltk.FeatStruct("[A= ?x, B= ?x]") # Exploring feature structures (fs1 and fs8)
 fs8 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
 fs1.unify(fs8) 
 fs1=nltk.FeatStruct("[A= ?x, B= ?x]") # subsume structures
 fs8 = nltk.FeatStruct("[B=k]")
 fs1.unify(fs8)

print fs1.unify(fs8)
