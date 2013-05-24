
import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"),
          ("both","DT"),("new","JJ"),("positions","NNS")]
# Chunk grammar
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}"
# Creating chunk parser
bk=nltk.RegexpParser(grammar)
# Examing the chunk on the example
result=bk.parse(sentence)
print result
from nltk.corpus import conll2000
# Creating a chunk parser and testing it on the example
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
# Printing results
print cp.evaluate(test_sents)
