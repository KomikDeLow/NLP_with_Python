# TODO
# The precision is very low.
#

# Fuyarchuk O. Chapter 7 Task 6
import nltk
sentence = [("July", "NNP"), ("and", "CC"), ("August", "NNP"), ("all", "DT"), ("your", "PRP$"),
            ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"), ("company", "NN"),
            ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")] #Sentence that should be chunked.
grammar = "NP:{<DT|PRP\$|NN.*>+<CC><NN.*>+}" #Define a grammar with the regular expression rules
cp=nltk.RegexpParser(grammar)#using grammar create a chunk parser and test
print cp.parse(sentence)
from nltk.corpus import conll2000 # import conll2000 corpus
cp=nltk.RegexpParser(grammar)# using grammar create a chunk parser and test
                             #it on our sentence
test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=('NP',))
print cp.evaluate(test_sents) # print evaluation result
