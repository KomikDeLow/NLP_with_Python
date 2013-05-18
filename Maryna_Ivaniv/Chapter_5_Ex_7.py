#Maryna Ivaniv PRLs-11 Chapter 5 Ex.7
#Create 2 dictionaries, d1 and d2, and add some entries to each.
#Now issue the command d1 update(d2).
#What did this do? What might it be useful for?

import nltk
from nltk import*
d1={}.fromkeys(['doll','sky', 'jump'])#create 1st dictionary 
d2={}.fromkeys(['deep','coast','sea'])#create 2nd dictionary
d1['doll']='N'#indicated a part of speech
d1['sky']='N'
d1['jump']='V'
d1['jump']='V'
d2['deep']='ADJ'
d2['coast']='N'
d2['sea']='N'
d1.update(d2)#updated the 1st dictionary by the 2nd dictionary 
d1
print d1 #printed the words from both dictionaries and parts of speech which were added
# This programe might be useful for creating one dictionary instead of several.
