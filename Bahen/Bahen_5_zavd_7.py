# TODO
# Comments?
# 
#
#Bahen Diana, PRLs-11, Chapter 5, Exercise 7

import nltk
from nltk import*
d1={}.fromkeys(['help', 'room', 'red'])
d2={}.fromkeys(['phone', 'ask', 'clean', 'member'])
#created two dictionaries and added entries to each
d1['help']='V'
d1['room']='N'
d1['red']='A'
d2['phone']='N'
d2['ask']='V'
d2['clean']='A'
d2['member']='N'
d1.update(d2)
#command update added words from d2 to d1. it can be useful for renewing the main dictionary
d1
print d1
