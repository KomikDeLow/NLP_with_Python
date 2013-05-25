#by Ivanna Kushniruk

import nltk
print 'if Angus sings, it is NOT the case that Bertie sulks: As -> -Bs'
lp = nltk.LogicParser()
As = lp.parse ('As') # Angus sings
NBs = lp.parse ('-Bs') # (NOT the case) Berite sulks
A = lp.parse('As -> -Bs') # if Angus sings, it is NOT the case that Bertie sulks
prover = nltk.Prover9()
print prover.prove (NBs, [As, A])

print 'Cyril runs and barks:Cr & Cb'
lp = nltk.LogicParser()
Cr = lp.parse('Cr') # Cyril runs
Cb = lp.parse('Cb') # Cyril barks
B = lp.parse('Cr & Cb') # Cyril runs and Cyril barks
prover = nltk.Prover9()
print prover.prove(Cr, [Cb, B])

print 'It will snow if it doesn’t rain: Sn -> -Rn'
lp = nltk.LogicParser()
Sn = lp.parse('Sn') # it will snow
NRn = lp.parse('-Rn') # it does NOT rain
C = lp.parse('Sn -> -Rn') # it will snow IF it does not rain
prover = nltk.Prover9()
print prover.prove(NRn, [Sn, C])


print 'It’s not the case that Irene will be happy if Olive or Tofu comes: -Ih -> Oc|Tc'
lp = nltk.LogicParser()
NIh = lp.parse('-Ih') # NOT the case Irene will be happy
Oc = lp.parse('Oc') # Olive comes
Tc = lp.parse('Tc') # Tofu comes
D = lp.parse('-Ih -> Oc|Tc') # NOT the case Irene will be happy IF Oliver comes OR Tofu comes
prover = nltk.Prover9()
print prover.prove(Oc|Tc, [NIh, D])

print 'Pat didn’t cough or sneeze: -Pc | -Ps'
lp = nltk.LogicParser()
NPc = lp.parse('-Pc') # Pat did NOT cough
NPs = lp.parse('-Ps') # Pat did NOT sneeze
E = lp.parse('-Pc | -Ps') # Pat did NOT cough OR Pat did NOT sneeze
prover = nltk.Prover9()
print prover.prove(E, [NPc, NPs])

print 'If you don’t come if I call, I won’t come if you call: (-Yc -> -Ic)->(-Ic -> Yc)'
lp = nltk.LogicParser()
NYco = lp.parse('-Yco') # You do NOT come
Ica = lp.parse ('Ica') # I call
NIco = lp.parse ('-Ico') # I do NOT come
Yca = lp.parse ('Yca') # You call
X = lp.parse ('-Yco -> Ica') # first part of sent with IF clause
Y = lp.parse ('-Ico -> Yca') # second part of sent with IF clause
Fin = lp.parse ('(-Yco -> Ica)->(-Ico -> Yca)')
# possible Fin = (-Yco -> Ica)<->(-Ico -> Yca) and Fin = -Yco -> Ica)&(-Ico -> Yca) both give True
prover = nltk.Prover9()
print prover.prove (Y, [X, Fin])







