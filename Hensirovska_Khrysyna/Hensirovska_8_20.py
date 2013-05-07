# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#Розділ 8,завдання 20
#To compare multiple trees in a single window, we can use the draw_trees()
#method. Define some trees and try it out:
#>>> from nltk.draw.tree import draw_trees
#>>> draw_trees(tree1, tree2, tree3)
#import nltk
#from nltk import tree
#Використовуємо метод draw_trees() для порівняння дерев у одному вікні
#from nltk.draw.tree import draw_trees
#Встановлюємо просту граматику для першого дерева
#groucho_grammar = nltk.parse_cfg("""
#S -> NP VP
#NP -> Det N
#VP -> VP AP | V NP
#AP -> Adj PropN
#Det -> 'The'
#N -> 'sun'
#V -> 'shines'
#Adj -> 'bright'
#PropN -> 'today'
#""")
#sent=['The','sun','shines','bright','today'] #будуємо речення
#parser = nltk.ChartParser(groucho_grammar) #проводимо аналіз 1 речення
#tree1 = parser.nbest_parse(sent)
#Встановлюємо просту граматику для другого дерева
#groucho_grammar2 = nltk.parse_cfg("""
 #S -> NP
# NP -> Adj NP
 #NP -> N Conj N
  #Conj -> 'and'
  # N -> 'orange' | 'banana'
   #Adj -> 'tasty'
   #""")
#parser2 = nltk.ChartParser(groucho_grammar2) #проводимо аналіз 2ого речення
#sent2=['tasty','orange','and','banana'] #будуємо речення
#tree2 = parser2.nbest_parse(sent2)
#Встановлюємо просту граматику для третього дерева
#groucho_grammar3 = nltk.parse_cfg("""
# S -> NP VP
 #NP -> Det N
 #VP -> VP AP | V NP
 #AP -> Adj PropN
 #Det -> 'The'
 #N -> 'students'|'points'
 #V -> 'expect'
 #Adj -> 'good'
 #PropN -> 'tomorrow'
 #""")
#sent3= ['The','students','expect','good','points','tomorrow'] #будуємо речення
#parser3 = nltk.ChartParser(groucho_grammar3)#проводимо аналіз 3ого речення
#tree3 = parser3.nbest_parse(sent3)
#draw_trees()
#draw_trees(tree1, tree2, tree3)
#виводимо  три дерева в одному вікні програми

