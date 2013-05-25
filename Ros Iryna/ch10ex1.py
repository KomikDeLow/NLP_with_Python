#Iryna Ros, PRLs-11, chapter 10, exercise 1
#Translate the following sentences into propositional logic and verify that they
#parse with LogicParser. Provide a key that shows how the propositional variables
#in your translation correspond to expressions of English.
#
# a. If Angus sings, it is not the case that Bertie sulks.
import nltk
lp = nltk.LogicParser ()
R = lp.parse('AnS -> -Bers') # AnS - Angus sings, -BerS - it is not a case that Bertie sulks
prover = nltk.Prover9()
print prover.prove(R)

# b. Cyril runs and barks.
import nltk
lp = nltk.LogicParser ()
R = lp.parse('CyR & CyrB') # CyR - Cyril runs, CyrB - Cyril barks
prover = nltk.Prover9()
print prover.prove(R)

# c. It will snow if it doesn’t rain.
import nltk
lp = nltk.LogicParser ()
SnF = lp.parse('Snow') # It will snow
NotRain = lp.parse ('-Rain') # it doesn't rain
R = lp.parse ('Snow -> -Rain')
prover = nltk.Prover9()
print prover.prove(R)

# d. It’s not the case that Irene will be happy if Olive or Tofu comes.
import nltk
lp = nltk.LogicParser ()
IreneNotHappy = lp.parse('-IreneHappy') # It’s not the case that Irene will be happy
OliveCom = lp.parse ('OliveCom') #Olive comes
TofuCom = lp.parse ('TofuCom') # Tofu comes
R = lp.parse ('-IreneHappy -> OliveCom | TofuCom')
prover = nltk.Prover9()
print prover.prove(R)
              
# e. Pat didn’t cough or sneeze.
import nltk
lp = nltk.LogicParser ()
R = lp.parse('-PatC | -PatS') # -PatC - Pat didn't cough, -PatS - Pat didn't sneeze
prover = nltk.Prover9()
print prover.prove(R)

# f. If you don’t come if I call, I won’t come if you call.
import nltk
lp = nltk.LogicParser ()
R = lp.parse('-iCome <-> -youCome') # -iCome - If you don’t come if I call,  -youCome - I won’t come if you call
prover = nltk.Prover9()
print prover.prove(R)
