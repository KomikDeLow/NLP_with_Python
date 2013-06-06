# Chapter_7_Ex_2_Mokhonova
import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"),
          ("both","DT"),("new","JJ"),("positions","NNS")]
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" # zadaju gramatyku
bk=nltk.RegexpParser(grammar)# stvorjuju syntaksychnyj̆ analizator
result=bk.parse(sentence)#testuju syntaksychnyj analizator
print result
from nltk.corpus import conll2000 # importuju korpus conll2000
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents) # vyvodzhu rezul'tat
