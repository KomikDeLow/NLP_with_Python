#Olesya Mykhaulyk
#ALs-12
#chapter 10 ex 1d
# It is not the case that Irene will be happy if Olive or Tofu comes.
import nltk
lp = nltk.LogicParser()
InbH=lp.parse('-IwbH')
OoTc=lp.parse('OoTc')
Irene=lp.parse('-IwbH -> OoTc')
prover = nltk.Prover9()
print prover.prove(OoTc, [InbH, Irene])
