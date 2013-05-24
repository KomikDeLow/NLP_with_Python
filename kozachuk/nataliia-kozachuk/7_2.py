#Nataliia_kozachuk, Chap7_Ex2
import nltk
sentence = [("many","JJ"),("researchers","NNS"), ("two","CD"),("weeks","NNS"), ("both", "DT"), ("new","JJ"),("positions","NNS"), ]
##stvoryemo rechenna
grammar = "NP:{<DT>*<CD>*<JJ>*<NN.*>+}"
#stvoryemo regyljarnuj vuraz, Chunk determiner/ number/adjective/noun
cp=nltk.RegexpParser (grammar)
#stvoryemo RegexpParser text ( RegexpParser works by defining rules for grouping different words together)
result = cp.parse (sentence)
print result
