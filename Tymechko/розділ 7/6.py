import nltk
sentence=[("July","NNP"),("and","CC"),("August","NNP"),("all","DT"),
          ("your","PRP$"),("managers","NNS"),("and","CC"),("supervisors","NNS"),
          ("company","NN"),("courts","NNS"),("and","CC"),("adjudicators","NNS")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()
