#Khrystyna Hensirovska,Als-12
#Chapter 10 task 1
#Translate the following sentences into propositional logic and verify that they
#parse with LogicParser. Provide a key that shows how the propositional variables
#in your translation correspond to expressions of English.
#a. If Angus sings, it is not the case that Bertie sulks.
#b. Cyril runs and barks.
#c. It will snow if it doesn’t rain.
#d. It’s not the case that Irene will be happy if Olive or Tofu comes.
#e. Pat didn’t cough or sneeze.
#f. If you don’t come if I call, I won’t come if you call.
import nltk
lp=nltk.LogicParser()
Angus=lp.parse ('Angus')
BertieNotS=lp.parse('-BerieS')
R=lp.parse('Angus & BertieS') #Angus- Angus sing,BertieS-it is not the case
#that Bertie sulks
prover=nltk.Prover9() #çä³éñíþº âèâ³ä,ìè çàäàºìî äàí³,à ô-êö³ÿ ïåðåâ³ðÿº ÷è
#ìîæíà âèâåñòè íîâå çíà÷åííÿ
prover.prove(BertieNotS,[Angus,R])
import nltk
lp=nltk.LogicParser()
R=lp.parse('CyrR & CyrB')# CyrR-Cyril runs,CyrB-Cyril barks
prover=nltk.Prover9()
prover.prove(R)

import nltk
lp=nltk.LogicParser()
SnF=lp.parse('Snow')#It will snow
NotRain=lp.parse('-Rain')#it doesn't rain
prover=nltk.Prover9()
prover.prove(NotRain,[SnF, R])

import nltk
lp=nltk.LogicParser()
IreneNotHappy=lp.parse('-IreneHappy')#It's not the case that Irene
#will be happy

OliveCom=lp.parse('OliveCom') #Olive comes
R=lp.parse('-IreneHappy-> OliveCom | TofuCom')#Tofu comes
prover=nltk.Prover9()
prover.prove(R)

import nltk
lp=nltk.LogicParser()
R=lp.parse('-PatC | -PatS') # -PatC-Pat didn't cough,PatS-Pat didn't sneeze
prover=nltk.Prover9()
prover.prove(R)

import nltk
lp=nltk.LogicParser()
R=lp.parse('-iCome <-> -youCome') #-iCome - If you don't come if I call
# -youCome - I won't come if you call
prover=nltk.Prover9()
prover.prove(R)

