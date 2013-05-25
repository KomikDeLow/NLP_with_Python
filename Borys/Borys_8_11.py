# Roman Borys PRLs-11
import nltk
from nltk import Tree
help(Tree) 
sentence= ['He','wants','drink'] # creating sentence
grammar1 = nltk.parse_cfg(""" 
   	S -> NP VP 
        NP -> "He" 
   	VP -> V NP 
   	V -> "wants" 
   	NP -> "drink" 
   	 """)

sentence= "He wants drink".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3) #parser
for tree in rd_parser.nbest_parse(sentence):
  print tree


