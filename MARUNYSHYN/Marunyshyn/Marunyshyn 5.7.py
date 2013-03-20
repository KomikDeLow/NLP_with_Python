# TODO
# Comments?
#

import nltk
from nltk import*
d1={}.fromkeys(['call','mother','home'])
d2={}.fromkeys(['speak','father','big'])
d1['call']='V'
d1['mother']='N'
d1['home']='N'
d2['speak']='V'
d2['father']='N'
d2['big']='A'
d1.update(d2)
d1
print d1
