import nltk
cfdist = nltk.ConditionalFreqDist()
def chunked_tags(train):
    """Generate a list of tags that tend to appear inside chunks"""
    for t in train:
        for word, tag, chtag in nltk.chunk.tree2conlltags(t):
            if chtag == "O":
                cfdist[tag].inc(True)
            else:
                cfdist[tag].inc(False)
    return [tag for tag in cfdist.conditions() if cfdist[tag].max() == True]

            
train_sents = nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('NP'))
print chunked_tags(train_sents)

#Отримали список тегів, які найчастіше не входять в іменниковий вираз.

import nltk
sentence = [("Rotatek", "NNP"), ("is", "VBZ"), ("the", "DT"),
            ("leader", "NN"), ("in", "IN"), ("offset", "JJ"),
            ("technology", "NN"), ("with", "IN"),("In-line", "JJ"),
            ("combination", "NN"), ("processes", "NNS"), ("for", "IN"),
            ("the", "DT"),("label", "NN"), ("industry", "NN"),  ("one", "CD"),
            ("of", "IN"), ("the", "DT"), ("fastest", "JJS"),
            ("developing", "VBG"), ("trends", "NNS"), ("today", "NN")]
grammar = r"""
        NP: 
        {<.*>+} # Chunk everything
	}<VBD|IN|CC|IN|MD|RB|RBR|RP|SYM|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WRB>+{
	"""
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result

            
