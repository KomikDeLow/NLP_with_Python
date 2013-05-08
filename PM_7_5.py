import nltk
# create a chunk grammar
grammar = """
NP: {<DT>?<VBG>*<NN>}
{<DT>?<VBG>*<NNS>}
{<DT>?<NN>*<VBG>}
{<NN>?<VBG>*<NN>}
"""
# using this grammar, create a chunk parser
cp = nltk.RegexpParser(grammar)
# define a sentence with gerunds to be chunked
sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"), ("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
# run the chunker on this input
print cp.parse(sentence)
# define a sentence of my own to be chunked
sentence = [("Mary", "NNP"), ("saw", "VBD"), ("the", "DT"), ("sitting", "VBG"), ("cat", "NN"), ("on", "IN"), ("the", "DT"), ("tree", "NN"), (".", "."), ("The", "DT"), ("following", "VBG"), ("phrases", "NNS"), ("concern", "VB"), ("the", "DT"), ("problem", "NN"), (".", "."), ("The", "DT"), ("developing", "VBG"), ("trends", "NNS"), ("fell", "VBD"), (".", "."), ("The", "DT"), ("price", "NN"), ("cutting", "VBG"), ("at", "IN"), ("3", "CD"), ("%", "NN"), (".", ".")]
# run the chunker on this input
print cp.parse(sentence)
