#Olesya Mykhaulyk
#ALs-12
#chapter 10 ex 1c
# It will snow if it doesn't rain.
import nltk
lp = nltk.LogicParser()
S=lp.parse('S')
R=lp.parse('-R')
C=lp.parse('S -> -R')
prover = nltk.Prover9()
print prover.prove(R, [C,S])
