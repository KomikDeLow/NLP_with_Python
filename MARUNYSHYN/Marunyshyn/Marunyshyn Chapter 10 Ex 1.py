# Irena Marunyshyn PRLs-12 Chapter 10 Ex 1
import nltk
sq=nltk.LogicParser()
Angus=sq.parse ('Angus')
BertieNotS=sq.parse('-BerieS')
R=sq.parse('Angus & BertieS') #Angus- Angus sing,BertieS-it is not the case
prover=nltk.Prover9()
print prover.prove(BertieNotS,[Angus,R])# # print if this sentence is logical

import nltk
sq=nltk.LogicParser()
R=sq.parse('CyrR & CyrB')# Cyril runs + Cyril barks
prover=nltk.Prover9()
print prover.prove(R)

import nltk
sq=nltk.LogicParser()
SnF=sq.parse('Snow')#It will snow 
NotRain=sq.parse('-Rain')# it doesn’t rain
prover=nltk.Prover9()
print prover.prove(NotRain,[SnF, R])

import nltk
sq=nltk.LogicParser()
IreneNotHappy=sq.parse('-IreneHappy') # It’s not the case that Irene will be happy
OliveCom=sq.parse('OliveCom')# Olive comes
R=sq.parse('-IreneHappy-> OliveCom | TofuCom')# Olive and Tofu come
prover=nltk.Prover9()
print prover.prove(R)


import nltk
sq=nltk.LogicParser()
R=sq.parse('-iCome <-> -youCome')#-iCome - If you don't come if I call
# -youCome - I won't come if you call
prover=nltk.Prover9()
print prover.prove(R)

import nltk
sq=nltk.LogicParser()
R=sq.parse('-PatC | -PatS')# -PatC-Pat didn't cough,PatS-Pat didn't sneeze
prover=nltk.Prover9()
# with the help of this program we can check if there is the logic of our sentences.
# if there is not that we can see false if there is that is true.
# we can know if our translation correspond to expressions of English.
print prover.prove(R)
