#Olesya Mykhaulyk
#ALs-12
#chapter 10 ex 1f
# If you don't come if I call, I won't come if you call.
import nltk
lp = nltk.LogicParser()
You=lp.parse('-A -> B')
I=lp.parse('-C -> D')
Conc=lp.parse('(-A -> B)<->(-C -> D)')
prover = nltk.Prover9()
print prover.prove(Conc, [You,I])
