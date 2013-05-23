#Olesya Mykhaulyk
#Als-12
# chapter 10 ex 1 b
# Cyril runs and barks.
import nltk
lp = nltk.LogicParser()
R=lp.parse('R')
B=lp.parse('B')
C=lp.parse('R & B')
prover = nltk.Prover9()
print prover.prove(B, [C])
