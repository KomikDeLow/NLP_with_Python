#Presented by Tkachuk Iryna

# 7_2 Write a tag pattern to match noun phrases containing plural head noun



import nltk
#some sentence
sentence=[("many", "JJ"), ("researches", "NNS"), (",", ","), ("two", "CD"),
          ("weeks", "NNS"), (",", ","), ("both", "DT"),("new", "JJ"),
          ("position", "NNS")]
#define grammar with regular expression rule
grammar="NP:{<DT|CD>?<JJ>*<NN.>}"
#create a chunk parser with defined grammar
cp=nltk.RegexpParser(grammar)
#present result
result=cp.parse(sentence)
print result
result.draw()
