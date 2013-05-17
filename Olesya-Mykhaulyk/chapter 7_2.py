#Olesya Mykhaulyk
#ALs-12
# Chapter 7 Ex.2 Corrected
import nltk
noun_phrases=[("many", "JJ"), ("researches", "NNS"),(",", ","), ("two", "CD"), 
             ("weeks", "NNS"),(",", ","), ("both", "DT"), ("new", "JJ"), 
   	     ("positions", "NNS")]

grammar="NP:{<DT>?<JJ>?<CD>?<NNS>}"
# we set grammar
cp=nltk.RegexpParser(grammar)
#chunk parsel
result=cp.parse(noun_phrases)
result.draw
