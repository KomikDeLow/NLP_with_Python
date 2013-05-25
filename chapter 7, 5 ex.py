import nltk
from nltk import RegexpParser

grammar = r"""
    NP: {<DT>?<VBG>?<NN>}
    NP: {<NN>?<VBG>?<NN>}
    NP: {<VBG>?<NN>}
    NP: {<NN>?<VBG>}"""
sentences = [[("The","DT"),("working","VBG"),("day","NN")],
             [("The","DT"),("Developing","VBG"),("Economies","NN")],
             [("The","DT"),("working","VBG"),("machine","NN")],
             [("Horse","NN"),("riding","VBG"),("rules","NN")],
             [("Air","NN"),("conditioning","VBG"),("systems","NN")],
             [("Freedom","NN"),("liking","VBG"),("people","NN")],
             [("Dying","VBG"),("swan","NN")],
             [("Deer","NN"),("hunting","VBG")],]

parser = RegexpParser(grammar)
for sent in sentences:
    print parser.parse(sent)
