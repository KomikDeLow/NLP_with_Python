
import nltk, re, pprint
sentence = [("the","DT"), ("little","JJ"),("doc", "NN"), ("barked","VBD"),("at","IN"),("the","DT"),("cat","NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar) 
result= cp.parse(sentence)
print result
from nltk.corpus import conll2000 
print conll2000.chunked_sents('train.txt',chunk_types = ['PP']) [59] 
test_sents = conll2000.chunked_sents('test.txt', chunk_types = ['PP'])
print cp.evaluate(test_sents) 
grammar = r"PP:{<[INNN].*>+}"
cp = nltk.RegexpParser(grammar) 
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
# на виході отримуємо речення з тегами, відповідно до слів