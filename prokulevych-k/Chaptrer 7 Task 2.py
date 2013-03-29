#Ïğîêóëåâè÷ Ê. ÏĞËñ-11, Ğîçä³ë 7, Çàäà÷à 2
#Regular expression–based NP chunker
import nltk
sentence = [("old", "JJ"), ("big", "JJ"), ("house", "NN"), ("ten", "CD"), ("miles", "NNS"), ("the", "DT"), ("red", "JJ"), ("apples", "NNS"), ("his", "PRP"), ("bag", "NN")]
grammar = "NP: {<DT>*<JJ>*<CD>*<PRP>*<NN.*>+}" # creating chunk grammar 
cp = nltk.RegexpParser(grammar)#create a chunk parser using a grammar
result = cp.parse(sentence)#test chunk parser on sentence
print result
