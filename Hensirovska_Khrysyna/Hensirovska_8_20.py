# TODO
# I need Python modul.
#

#����������� ��������,����-12
#����� 8,�������� 20
#To compare multiple trees in a single window, we can use the draw_trees()
#method. Define some trees and try it out:
#>>> from nltk.draw.tree import draw_trees
#>>> draw_trees(tree1, tree2, tree3)
#import nltk
#from nltk import tree
#������������� ����� draw_trees() ��� ��������� ����� � ������ ���
#from nltk.draw.tree import draw_trees
#������������ ������ ��������� ��� ������� ������
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
#sent=['The','sun','shines','bright','today'] #������ �������
#parser = nltk.ChartParser(groucho_grammar) #��������� ����� 1 �������
#tree1 = parser.nbest_parse(sent)
#������������ ������ ��������� ��� ������� ������
#groucho_grammar2 = nltk.parse_cfg("""
 #S -> NP
# NP -> Adj NP
 #NP -> N Conj N
  #Conj -> 'and'
  # N -> 'orange' | 'banana'
   #Adj -> 'tasty'
   #""")
#parser2 = nltk.ChartParser(groucho_grammar2) #��������� ����� 2��� �������
#sent2=['tasty','orange','and','banana'] #������ �������
#tree2 = parser2.nbest_parse(sent2)
#������������ ������ ��������� ��� �������� ������
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
#sent3= ['The','students','expect','good','points','tomorrow'] #������ �������
#parser3 = nltk.ChartParser(groucho_grammar3)#��������� ����� 3��� �������
#tree3 = parser3.nbest_parse(sent3)
#draw_trees()
#draw_trees(tree1, tree2, tree3)
#��������  ��� ������ � ������ ��� ��������

