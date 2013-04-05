#Прокулевич К. ПРЛс-11, Розділ 7, Задача 6
#A chunker that handles NP
import nltk
grammar = r"""
       NP:{<DT|PRP/$|NN.*>+<CC><NN.*>*} #Chunk sequences of DT, PRP, NN, CC
       """
cp = nltk.RegexpParser(grammar)
sentence=[("July", "NNP"), ("and", "CC"), ("August", "NNP"), ("all", "DT"), ("your", "PRP$"),
("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"), ("company", "NN"), ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")]
cp.parse(sentence)
from nltk.corpus import conll2000
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)
