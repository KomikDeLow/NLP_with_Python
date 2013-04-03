#TODO
# Test your program on real sentences with NP that consist with JJ JJ NN...
#
#Прокулевич К. ПРЛс-11, Розділ 7, Задача 2
#Regular expression–based NP chunker
import nltk
sentence = [("many", "JJ"), ("researchers", "NNS"), ("two", "CD"), ("weeks", "NNS"), ("both", "DT"), ("new", "JJ"), ("positions", "NNS")]
grammar = "NP: {<DT>*<JJ>*<CD>*<PRP>*<NN.*>+}" # creating chunk grammar 
cp = nltk.RegexpParser(grammar)#create a chunk parser using a grammar
result = cp.parse(sentence)#test chunk parser on sentence
print result
