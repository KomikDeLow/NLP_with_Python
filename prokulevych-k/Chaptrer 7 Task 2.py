#TODO
# Test your program on real sentences with NP that consist with JJ JJ NN...
#
#Ïğîêóëåâè÷ Ê. ÏĞËñ-11, Ğîçä³ë 7, Çàäà÷à 2
#Regular expression–based NP chunker
import nltk
sentence=[("Jim", "NNP"), ("saw", "VBD"), ("beautiful", "JJ"), ("red", "JJ"), ("flowers", "NNS"), ("in", "IN"), ("the", "DT"), ("garden","NN")]
grammar = "NP: {<DT>*<JJ>*<NN.*>+}" # creating chunk grammar 
cp = nltk.RegexpParser(grammar)#create a chunk parser using a grammar
result = cp.parse(sentence)#test chunk parser on sentence
print result
