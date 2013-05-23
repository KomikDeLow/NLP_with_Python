#Olesya Mykhaulyk
#Als-12
#chapter 10 ex 1a
# If Angus sings it is not the case that Bertie sulks.
import nltk
lp=nltk.LogicParser()
A=lp.parse('A')
B=lp.parse('-B')
c=('A & -B')
prover=nltk.Prover9()
print prover.prove(A,[c])
