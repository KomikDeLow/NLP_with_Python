#Olesya Mykhaulyk
#ALs-12
#chapter 10 ex 1e
# Pat didn't cough or sneeze.
import nltk
lp = nltk.LogicParser()
S=lp.parse('-S')
C=lp.parse('-C')
Con=lp.parse('-S | -C')
prover = nltk.Prover9()
print prover.prove(Con, [C,S])
