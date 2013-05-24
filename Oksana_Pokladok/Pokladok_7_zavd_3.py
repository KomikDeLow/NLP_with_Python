#Oksana Pokladok
import nltk, re, pprint
sentence = [("the","DT"), ("little","JJ"), ("scared","JJ"),("girl", "NN"), ("pointed","VBD"),("to","IN"),("the","DT"),("windiw","NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar) # Chunk parser
result= cp.parse(sentence)
print result # Printing the result
from nltk.corpus import conll2000
print conll2000.chunked_sents('train.txt',chunk_types = ['PP']) [49] # Printing the 50th sentence from the training set
test_sents = conll2000.chunked_sents('test.txt', chunk_types = ['PP'])
print cp.evaluate(test_sents) # Printing ChunkParse score
grammar = r"PP:{<[INNN].*>+}"
cp = nltk.RegexpParser(grammar) #Chunk parser
print cp.evaluate(test_sents)
grammar = r"PP:{<IN><DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar=r"PP:{<NN>?<VB.*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP:{<VB.*>?<NN.*>*<DT>*}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)

# IOB accuracy indicates.
# When it did not find any chunks, Precision, Recall and F-Measure are all 0.