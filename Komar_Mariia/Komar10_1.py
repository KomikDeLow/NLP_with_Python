# Komar Mariia ALs-11
# Chapter_10, Ex_1

#Translate the following sentences into propositional logic and verify that
#they parse with LogicParser. Provide a key that shows how the propositional
#variables in your translation correspond to expressions of English.

# a. If Angus sings it is not the case that Bertie sulks.
# If [Angus sings] it is not the case that [Bertie sulks.]
# AngS-> Angus sings, BerS-> Bertie sulks
# AngS-> -BerS
import nltk
lp = nltk.LogicParser()
AngS= lp.parse('AngS')
NotBerS= lp.parse('-BerS')
R= lp.parse('AngS -> -BerS')
prover = nltk.Prover9() #але Prover9 в мене щось не працює
                        #Я також пробувала приклад з книжки, і він не працює
print prover.prove(NotBerS, [AngS, R])

# b. Cyril runs and barks.
# [Cyril runs] and [barks.]
# CyrR->Cyril runs, CyrB->Cyril barks
# CyrR & CyrB
import nltk
lp = nltk.LogicParser()
CyrR=lp.parse('CyrR')
CyrB=lp.parse('CyrB')
R=lp.parse('CyrR & CyrB')
prover = nltk.Prover9()# так само як і в попередньому - непрацює
print prover.prove(CyrB, [CyrR, R])

# c. It will snow if it doesn't rain.
# [It will snow] if it doesn't [rain.]
# ItS->It will snow, ItR-> rain
# -ItR -> ItS
import nltk
lp = nltk.LogicParser()
ItS=lp.parse('ItS')
ItR=lp.parse('-ItR')
R=lp.parse('-ItR -> ItS')
prover = nltk.Prover9()# так само як і в попередньому - непрацює
print prover.prove(ItS, [ItR, R])

# d. It is not the case that Irene will be happy if Olive or Tofu comes.
# It is not the case that [Irene will be happy] if [Olive] or [Tofu comes.]
#IrBH->Irene will be happy, OlC->Olive comes, ToC->Tofu comes
# -IrBH -> (OlC|ToC)
import nltk
lp = nltk.LogicParser()
IrBH=lp.parse('-IrBH')
OlC=lp.parse('OlC')
ToC=lp.parse('ToC')
R=lp.parse('-IrBH -> (OlC|ToC)')
prover = nltk.Prover9()# так само як і в попередньому - непрацює
print prover.prove(ToC, OlC, [IrBH, R])

# e. Pat didn't cough or sneeze.
# [Pat] didn't [cough] or [sneeze].
# PaC-> Pat cough, PaS->Pat sneeze
# -PaC|PaS
import nltk
lp = nltk.LogicParser()
PaC=lp.parse('-PaC')
PaS=lp.parse('PaS')
R=lp.parse('-PaC|PaS')
prover = nltk.Prover9()# так само як і в попередньому - непрацює
print prover.prove(PaS, [PaC, R])

# f. If you don't come if I call, I won't come if you call.
# If [you] don't [come] if [I call], [I] won't [come] if [you call.]
# YCo-> you come, ICa-> I call, ICo->I come, YCa-> you call
# (-YCo->ICa) <-> (-ICo->YCa)
import nltk
lp = nltk.LogicParser()
Frst=lp.parse('-YCo -> ICa')
Scnd=lp.parse('-ICo -> YCa')
Rf=lp.parse('(-A -> B)<->(-C -> D)')
prover = nltk.Prover9()# так само як і в попередньому - непрацює
print prover.prove(Scnd, [Frst, Rf])
