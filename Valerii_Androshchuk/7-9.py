# Valerii Androshchuk 7-9

import nltk
from random import shuffle
grammar = r"NP: {<DT|JJ|NN>+}"
cp = nltk.RegexpParser(grammar)
cs = nltk.chunk.ChunkScore()
for file in nltk.corpus.treebank_chunk.files()[:5]:
    for cs in nltk.corpus.treebunk.chunked_sents(file):
        ts = cp.parse(chunk_struct.flatten())
        cs.score(chunk_struct, ts)

no_error = cs.correct()
shuffle(no_error)
print incorrect[:30]
