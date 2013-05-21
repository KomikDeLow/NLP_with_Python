import nltk
sentence = [("many","JJ"),("researches","NNS"),(",",","),("two","CD"),
            ("weeks","NNS"),(",",","),("both","DT"),("new","JJ"),
            ("positions","NNS")]
grammar = "NP: {<DT|CD>?<JJ>*<NN.>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()
#У вікні NLTK зображені іменникові вирази, що включають в себе іменники множини.
