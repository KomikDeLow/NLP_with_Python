# Propositional Logic
# Halyna Khimka
# Chapter 10.1

import nltk
from nltk.sem.drt import DrtParser
from nltk.sem import logic
logic._counter._value = 0

# a) If Angus sings, it is not the case that Bertie sulks
# ang - Angus sings
# -brt - it is not the case that Bertie sulks

lp=nltk.LogicParser()
ang=lp.parse('ang')
brt=lp.parse('-brt')
S=lp.parse('ang ->brt')
print 'If Angus sings, it is not the case that Bertie sulks:', S
prover = nltk.Prover9()
print prover.prove(brt, [ang, S])

# b) Cyril runs and barks.
# Cr- Cyril runs
# Cb - Cyril barks

lp = nltk.LogicParser()
Cr = lp.parse('Cr')
Cb = lp.parse('Cb')
C = lp.parse('Cr & Cb')
print 'Cyril runs and barks:', C
prover = nltk.Prover9()
print prover.prove(Cr, [C])


# c) It will snow if it doesn’t rain.
# Sn - It will snow
# Rn - it rains
lp = nltk.LogicParser()
Sn=lp.parse('Sn')
Rn=lp.parse('-Rn')
R=lp.parse('Sn -> -Rn')
print 'It will snow if it doesn’t rain: ', R
prover = nltk.Prover9()
print prover.prove(Rn, [Sn, R])

# or
lp = nltk.LogicParser()
Sn=lp.parse('-Sn')
Rn=lp.parse('Rn')
R1=lp.parse('-Sn -> Rn')
print 'It will snow if it doesn’t rain: ', R1
prover = nltk.Prover9()
print prover.prove(Sn, [Rn, R])


# d) It’s not the case that Irene will be happy if Olive or Tofu comes.
# Ir - Irene will be happy
# Ol - Olive comes
# Tf - Tofu comes
lp = nltk.LogicParser()
Ir=lp.parse('-Ir')
Ol=lp.parse('Ol')
Tf=lp.parse('Tf')
Unhap=lp.parse('Ol|Tf')
IrHap=lp.parse('-Ir -> Ol|Tf')
print 'It’s not the case that Irene will be happy if Olive or Tofu comes.', IrHap
prover = nltk.Prover9()
print "d.", prover.prove(Unhap, [Ir, IrHap])

#e) Pat didn’t cough or sneeze.
# C - Pat cough
# S - Pat sneezed
lp = nltk.LogicParser()
C=lp.parse('-C')
S=lp.parse('-S')
P=lp.parse('-C|-S')
print 'Pat didn’t cough or sneeze.', P
prover = nltk.Prover9()
print prover.prove(P, [C, S])

# f) If you don’t come if I call, I won’t come if you call.
# Ycm - You come
# Ic - I call
# Icm - i will come
# Yc - you call

lp = nltk.LogicParser()
Ycm=lp.parse('-Ycm')
Ic=lp.parse('Ic')
Icm=lp.parse('-Icm')
Yc=lp.parse('Yc')
YNotCome=lp.parse('-Ycm -> Ic')
INotCome=lp.parse('-Icm -> Yc')
Utter=lp.parse('(-Ycm -> Ic) <-> (-Icm -> Yc)')
print 'If you don’t come if I call, I won’t come if you call.', Utter
prover = nltk.Prover9()
print "f.", prover.prove(Utter, [YNotCome, INotCome])
