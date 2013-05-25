# Valerii Androshchuk APL(s)-13.
# Chapter 10, Task 1.
# Tranlsate the following sentences into propsional logic and verify
# that parse with LogicParser. Provide a key that shows how the
# propositional variables in your translation correspond to expression
# of English. 

# a)If Angus sings, it is not the case that Bertie sulks.
import nltk
lp = nltk.LogicParser()
An= lp.parse('An')
Be= lp.parse('-Be')
A= lp.parse('An & -Be')
prover = nltk.Prover9()
print prover.prove(An, [A,Be])

# b)Cyril runs and barks.
import nltk
lp = nltk.LogicParser()
CR=lp.parse('CR')
CB=lp.parse('CB')
R=lp.parse('CR & CB')
prover = nltk.Prover9()
print prover.prove(R, [CB, CR])

# c)It will snow if it doesn’t rain.
import nltk
lp = nltk.LogicParser()
Sn=lp.parse('S')
Ra=lp.parse('-R')
C=lp.parse('S -> -R')
prover = nltk.Prover9()
print prover.prove(Ra, [C, Sn])

# d)It’s not the case that Irene will be happy if Olive or Tofu comes.
import nltk
lp = nltk.LogicParser()
In=lp.parse('-IwbH')
Tc=lp.parse('Tc')
Irene=lp.parse('-IwbH -> Tc')
prover = nltk.Prover9()
print prover.prove(Irene, [In, Tc ])

# e)Pat didn’t cough or sneeze.
import nltk
lp = nltk.LogicParser()
Sn=lp.parse('-S')
Cou=lp.parse('-C')
P=lp.parse('-S | -C')
prover = nltk.Prover9()
print prover.prove(P, [Cou, Sn])

# f)If you don’t come if I call, I won’t come if you call.
import nltk
lp = nltk.LogicParser()
Fi=lp.parse('-A -> B')
S=lp.parse('-C -> D')
End=lp.parse('(-A -> B)<->(-C -> D)')
prover = nltk.Prover9()
print prover.prove(End, [S, Fi])
print prover.prove(End)

