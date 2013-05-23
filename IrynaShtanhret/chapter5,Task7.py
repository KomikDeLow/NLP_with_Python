#Штангрет Ірина, ПРЛс-13, завдання 7
import nltk
from nltk import*
d1={}.fromkeys(['want', 'be', 'like'])#stvoryla slovnyk 1
d2={}.fromkeys(['winter', 'summer', 'weather', 'girl', 'tiger'])#stvoryla slovnyk 2
d1['want']='V'#nadala znachennya kozhnomu slovu
d1['be']='V'
d1['like']='V'
d2['winter']='N'
d2['summer']='N'
d2['weather']='N'
d2['girl']='N'
d2['tiger']='N'
d1.update(d2)#slovnyk 1 dopovnyvsya 2
print d1
#{'be': 'V', 'like': 'V', 'summer': 'N', 'tiger': 'N', 'weather': 'N', 'want': 'V', 'girl': 'N', 'winter': 'N'}

