import nltk
from nltk import RegexpParser
from nltk.corpus import conll2000

for snt in conll2000.chunked_sents("test.txt", chunk_types=["NP"])[:5]:
    print snt 
grammar = "NP: {<DT>?<JJ>*<NN>}"
sentence = [("the","DT"),("little","JJ"),("yellow","JJ"),
            ("dog","NN"),("barked","VBD"),("at","IN"),
            ("the","DT"),("cat","NN")]
parser = RegexpParser(grammar)
print parser.parse(sentence)
