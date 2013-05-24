# Ivanna Kushniruk

import nltk
#define sentence
sentence=[("many", "JJ"), ("researches", "NNS"), (",", ","), ("two", "CD"),
          ("weeks", "NNS"), (",", ","), ("both", "DT"),("new", "JJ"),
          ("position", "NNS")]
grammar="NP:{<DT|CD>?<JJ>*<NN.>}" #define grammar with regular expressions
cp=nltk.RegexpParser(grammar)#create a chunk parser 
result=cp.parse(sentence)#present parser
print result

