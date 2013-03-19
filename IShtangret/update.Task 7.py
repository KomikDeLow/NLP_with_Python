# TODO
# Your dict hasn't a values
# You must correct the text of program

#пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅ, пїЅпїЅпїЅпїЅ-13, пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ 7
d1={}.fromkeys(['want', 'be', 'like']) # пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅ 1
d2={}.fromkeys(['winter', 'summer', 'weather', 'girl', 'tiger'])# пїЅпїЅпїЅпїЅпїЅпїЅпїЅ 2
d1.update(d2)#пїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅ update пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ 2 пїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ 1
sorted(d1)
['be', 'girl', 'like', 'summer', 'tiger', 'want', 'weather', 'winter']#пїЅпїЅпїЅпїЅпїЅпїЅпїЅ 1 пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅ

#=======
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
d1
{'be': 'V', 'like': 'V', 'summer': 'N', 'tiger': 'N', 'weather': 'N', 'want': 'V', 'girl': 'N', 'winter': 'N'}

