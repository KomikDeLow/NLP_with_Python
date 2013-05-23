# -*- coding: cp1251 -*-
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
lp = nltk.LogicParser()
AngS= lp.parse('AngS')
NotBerS= lp.parse('-BerS')
R= lp.parse('AngS -> -BerS')#Angus- Angus sing,BertieS-it is not the case
#that Bertie sulks
prover = nltk.Prover9()#здійснює вивід,ми задаємо дані,а ф-кція перевіряє чи
#можна вивести нове значення
print prover.prove(NotBerS, [AngS, R])
import nltk
lp = nltk.LogicParser()
CyrR=lp.parse('CyrR')
CyrB=lp.parse('CyrB')
R=lp.parse('CyrR & CyrB')# CyrR-Cyril runs,CyrB-Cyril barks
prover = nltk.Prover9()
print prover.prove(CyrB, [CyrR, R])

import nltk
lp = nltk.LogicParser()
ItS=lp.parse('ItS')#It will snow
ItR=lp.parse('-ItR')#it doesn't rain
R=lp.parse('-ItR -> ItS')
prover = nltk.Prover9()
print prover.prove(ItS, [ItR, R])

import nltk
lp = nltk.LogicParser()
IrBH=lp.parse('-IrBH')
OlC=lp.parse('OlC')
ToC=lp.parse('ToC')
R=lp.parse('-IrBH -> (OlC|ToC)')#It's not the case that Irene
#will be happy if Olive or Tofu comes
prover = nltk.Prover9()
print prover.prove(ToC, OlC, [IrBH, R])

import nltk
lp = nltk.LogicParser()
PaC=lp.parse('-PaC')
PaS=lp.parse('PaS')
R=lp.parse('-PaC|PaS')# -PatC-Pat didn't cough,PatS-Pat didn't sneeze
prover = nltk.Prover9()
print prover.prove(PaS, [PaC, R])

import nltk
lp = nltk.LogicParser()
Frst=lp.parse('-YCo -> ICa')
Scnd=lp.parse('-ICo -> YCa')
Rf=lp.parse('(-A -> B)<->(-C -> D)') #-A - If you don't come if I call
# -B - I won't come if you call
prover = nltk.Prover9()
print prover.prove(Scnd, [Frst, Rf])
