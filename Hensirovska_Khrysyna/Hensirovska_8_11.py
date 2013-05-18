# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#Розділ 8,завдання 11
#With pen and paper, manually trace the execution of a recursive descent parser
#and a shift-reduce parser, for a CFG you have already seen, or one of your own
#devising.
import nltk
from nltk import Tree
help(Tree) #виводиться стрічка документації функції Tree
sentence= ['He','wants','drink'] #створюємо речення
#встановлюємо для речення просту граматику
grammar1 = nltk.parse_cfg("""  
   	#S -> NP VP 
   	#NP -> "He" 
   	#VP -> V NP 
   	#V -> "wants" 
   	#NP -> "drink" 
   	# """)

sentence= "He wants drink".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3) #програма синтак-
   	#сичного аналізу
   	#виводимо на екран синтаксичний аналіз
for tree in rd_parser.nbest_parse(sentence):
   print tree
 #виводимо на екран графічне зображення дерева
result.draw()

