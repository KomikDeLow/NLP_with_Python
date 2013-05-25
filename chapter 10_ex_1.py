# Iuliia Tsymbalista ALs-13
# chapter 10, ex. 1


#Translate the following sentences into propositional logic and verify
#that they parse with LogicParser. Provide a key that shows how
#the propositional variablesin your translation correspond to expressions of English.


import nltk
from nltk import *

# for this tas we should divide the sentences into segments

# a) If Angus sings, it is not the case that Bertie sulks
lp = nltk.LogicParser()
#ags - Angus sing
#-bs - it is not the case that Bertie sulks
ags = lp.parse('ags')
notbs = lp.parse('-bs')
R = lp.parse('ags -> -bs')
prover = nltk.Prover9()
prover.prove(notbs, [ags, R])


#b) Cyril runs and barks
lp = nltk.LogicParser()
#cr - Cyril runs
#cb - Cyril barks
cr = lp.parse('cr')
cb = lp.parse('cb')
R = lp.parse('cr & cb')
prover = nltk.Prover9()
prover.prove(R, [cr, cb])

#c) It will snow if it doesn’t rain
lp = nltk.LogicParser()
# sn - It will snow
# -ra - It doesn't rain
sn = lp.parse('sn')
notra = lp.parse('-ra')
R = lp.parse('sn -> -ra')
prover = nltk.Prover9()
prover.prove(sn, [notra, R])

#d) It’s not the case that Irene will be happy if Olive or Tofu comes
lp = nltk.LogicParser()
# -ir - It’s not the case that Irene will be happy
# oc - if Olive comes
# tc - if Tofu comes
nothappyir = lp.parse('-ir')
oc = lp.parse('oc')
tc = lp.parse('tc')
R = lp.parse('-ir -> oc | tc')
prover = nltk.Prover9()
prover.prove(R)


#e) Pat didn’t cough or sneeze
lp = nltk.LogicParser()
# -pc - Pat didn't cough
# -ps - Pat didn't sneeze
notpc = lp.parse('-pc')
notps = lp.parse('-ps')
R = lp.parse('-pc | -ps')
prover = nltk.Prover9()
prover.prove(R, [notpc, notps])

#f) If you don’t come if I call, I won’t come if you call
lp = nltk.LogicParser()
# -yc - If you don’t come
# icall - if I call
# -ic - I won’t come
# ycall - if you call
notyc = lp.parse('-yc')
icall = lp.parse('icall')
notic = lp.parse('-ic')
ycall = lp.parse('ycall')
R = lp.parse('(-yc -> icall) -> (-ic -> ycall)')
prover = nltk.Prover9()
prover.prove(R)


