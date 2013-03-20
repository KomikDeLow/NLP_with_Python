# TODO
# Comments?
# 
#

import nltk
from nltk import*
d1={}.fromkeys(['help', 'room', 'red'])
d2={}.fromkeys(['phone', 'ask', 'clean', 'member'])
d1['help']='V'
d1['room']='N'
d1['red']='A'
d2['phone']='N'
d2['ask']='V'
d2['clean']='A'
d2['member']='N'
d1.update(d2)
d1
print d1
