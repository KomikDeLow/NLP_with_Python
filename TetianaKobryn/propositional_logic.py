#Presented by Tetiana Kobryn
#
#Chapter 10, Ex.1
#Translate the following sentences into propositional logic and verify that they
#parse with LogicParser. Provide a key that shows how the propositional variables
#in your translation correspond to expressions of English.


import nltk
"""a. If Angus sings, it is not the case that Bertie sulks.
As -> -Bs"""
lp = nltk.LogicParser()
As = lp.parse('As')
Bs = lp.parse('-Bs')
R = lp.parse('As -> -Bs')
prover = nltk.Prover9()
prover.prove(Bs, [As, R])

"""b. Cyril runs and barks.
Cr & Cb"""
lp = nltk.LogicParser()
Cr = lp.parse('Cr')
Cb = lp.parse('Cb')
B = lp.parse('Cr & Cb')
prover = nltk.Prover9()
prover.prove(Cr, [B])

"""c. It will snow if it doesn’t rain.
Sn -> -Rn"""
lp = nltk.LogicParser()
Sn = lp.parse('Sn')
NotRn = lp.parse('-Rn')
C = lp.parse('Sn -> -Rn')
prover = nltk.Prover9()
prover.prove(Rn, [Sn, C])

"""d. It’s not the case that Irene will be happy if Olive or Tofu comes.
-Ih -> Oc|Tc"""
lp = nltk.LogicParser()
NotIh = lp.parse('-Ih')
Oc = lp.parse('Oc')
Tc = lp.parse('Tc')
OoT = lp.parse('Oc|Tc')
D = lp.parse('-Ih -> Oc|Tc')
prover = nltk.Prover9()
prover.prove(OoT, [NotIh, D])

"""e. Pat didn’t cough or sneeze.
-Pc | -Ps"""
lp = nltk.LogicParser()
NotC = lp.parse('-Pc')
NotS = lp.parse('-Ps')
E = lp.parse('-Pc | -Ps')
prover = nltk.Prover9()
prover.prove(E, [NotC, NotS])

"""f. If you don’t come if I call, I won’t come if you call.
(-Yc -> -Ic)<->(-Ic -> Yc)"""
lp = nltk.LogicParser()
YNotcome = lp.parse('-Yc -> -Ic')
INotcome = lp.parse('-Ic->Yc')
All = lp.parse('(-Yc -> -Ic)<->(-Ic -> Yc)')
prover = nltk.Prover9()
prover.prove(All, [YNotcome, INotcome])
