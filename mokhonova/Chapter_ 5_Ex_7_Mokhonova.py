#Chapter_5_Ex_7_Mokhonova
import nltk
from nltk import*
d1={}.fromkeys(['mother','key', 'call'])# stvorjuju slovnyk 1
d2={}.fromkeys(['see','beutiful','cat'])# stvorjuju slovnyk 2
d1['mother']='N'# dodaju chastynu movy
d1['key']='N'
d1['call']='V'
d2['see']='V'
d2['beutiful']='A'
d2['cat']='N'
d1.update(d2)# onovlennya
d1
print d1 # vuvedennya resul'tatu
