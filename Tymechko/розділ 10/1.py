#a If Angus sings, it is not the case that Bertie sulks
import nltk
lp = nltk.LogicParser()
#Ans - Angus sing
#-BerS - it is not the case that Bertie sulks
R = lp.parse('AnS -> -BerS')
prover = nltk.Prover9()
prover.prove(R)

#b Cyril runs and barks
import nltk
lp = nltk.LogicParser()
#CyR - Cyril runs
#CyrB - Cyril barks
R = lp.parse('CyR & CyrB')
prover = nltk.Prover9()
prover.prove(R)

#c It will snow if it doesn’t rain
import nltk
lp = nltk.LogicParser()
#It will snow
#It doesn't rain
SnF = lp.parse('Snow')
NotRain = lp.parse('-Rain')
R = lp.parse('Snow -> -Rain')
prover = nltk.Prover9()
prover.prove(NotRain, [Snow, R])

#d It’s not the case that Irene will be happy if Olive or Tofu comes
import nltk
lp = nltk.LogicParser()
#It’s not the case that Irene will be happy
IreneNotHappy = lp.parse('-IreneHappy')
#Olive comes
OliveCom = lp.parse('OliveCom')
#Tofu comes
TofuCom = lp.parse('TofuCom')
R = lp.parse('IreneHappy -> OliveCom | TofuCom')
prover = nltk.Prover9()
prover.prove(R)

#e Pat didn’t cough or sneeze
import nltk
lp = nltk.LogicParser()
# -PatC - Pat didn't cough
# -PatC - Pat didn't sneeze
R = lp.parse('-PatC | -PatS')
prover = nltk.Prover9()
prover.prove(R)

#f If you don’t come if I call, I won’t come if you call
import nltk
lp = nltk.LogicParser()
# -iCome - If you don't come if I call
# -youCome - I won't come if you call
R = lp.parse('-iCome <-> -youCome')
prover = nltk.Prover9()
prover.prove(R)
