# fine
#
#Irena Marunyshyn PRLs-12 Chapter 5 Ex7
import nltk
from nltk import*
d1={}.fromkeys(['mother','key', 'call'])# created dictionary1
d2={}.fromkeys(['see','beutiful','cat'])# created dictionary2
d1['mother']='N'# added part of speech
d1['key']='N'
d1['call']='V'
d2['see']='V'
d2['beutiful']='A'
d2['cat']='N'
d1.update(d2)# updating dictionary1 by dictionary 2
d1
print d1# print result. 2 dictionaries with their added part of speeches
