import nltk
sentence = [("many", "JJ"), ("researches", "NNS"),(",", ","), ("two", "CD"),
            ("weeks", "NNS"),(",", ","), ("both", "DT"), ("new", "JJ"),
            ("positions", "NNS")]
grammar = "NP: {<DT|CD>?<JJ>*<NN.>}" #Setting grammar rule
cp = nltk.RegexpParser(grammar) #Creating chunk parser.
result = cp.parse(sentence)
print result
result.draw()
