# Fuyarchuk O. Chapter 10 Task 1
# a. If Angus sings, it is not the case that Bertie sulks.
import nltk
lp = nltk.LogicParser()
As = lp.parse('As')
Bs = lp.parse('-Bs')
Z = lp.parse('As -> -Bs')
prover = nltk.Prover9()
print prover.prove(As, [Z])

# b. Cyril runs and barks.
lp = nltk.LogicParser()
Cr = lp.parse('Cr')
Cb = lp.parse('Cb')
K = lp.parse('Cr & Cb')
prover = nltk.Prover9()
print prover.prove(Cr, [K])

#c. It will snow if it doesn’t rain.
lp = nltk.LogicParser()
Sn = lp.parse('S')
NRn = lp.parse('-R')
F = lp.parse('S -> -R')
prover = nltk.Prover9()
print prover.prove(NRn, [Sn, F])

# d. It’s not the case that Irene will be happy if Olive or Tofu comes.
lp = nltk.LogicParser()
NIrn = lp.parse('-Irn')
Oc = lp.parse('Oc')
Tc = lp.parse('Tc')
OoT = lp.parse('Oc|Tc')
D = lp.parse('-Irn -> Oc|Tc')
prover = nltk.Prover9()
print prover.prove(OoT, [NIrn, D])

#e. Pat didn’t cough or sneeze.
lp = nltk.LogicParser()
NC = lp.parse('-Pc')
NS = lp.parse('-Ps')
M = lp.parse('-Pc | -Ps')
prover = nltk.Prover9()
print prover.prove(M, [NC, NS])

# f. If you don’t come if I call, I won’t come if you call.
lp = nltk.LogicParser()
ONE = lp.parse('-G -> D')
TWO = lp.parse('-V->R')
TOGETHER = lp.parse('(-G -> D)<->(-V -> R)')
prover = nltk.Prover9()
print  prover.prove(TOGETHER, [ONE, TWO])
