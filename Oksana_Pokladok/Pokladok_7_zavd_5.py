import nltk
grammar = """  # I create a chunk grammar
NP: {<DT>?<VBG>*<NN>}
{<DT>?<VBG>*<NNS>}
{<DT>?<NN>*<VBG>}
{<NN>?<VBG>*<NN>}
"""
cp = nltk.RegexpParser(grammar) # using this grammar, I create a chunk parser
# define a sentence with gerunds to be chunked
sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"), ("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
# run the chunker on this input
print cp.parse(sentence)
# define a sentence of my own to be chunked
sentence = [("Jane", "NNP"), ("saw", "VBD"), ("the", "DT"), ("sitting", "VBG"), ("dog", "NN"), ("on", "IN"), ("the", "DT"), ("street", "NN"), (".", "."), ("The", "DT"), ("following", "VBG"), ("phrases", "NNS"), ("concern", "VB"), ("the", "DT"), ("problem", "NN"), (".", "."), ("The", "DT"), ("developing", "VBG"), ("countries", "NNS"), ("grow", "VBD"), (".", "."), ("The", "DT"), ("price", "NN"), ("cutting", "VBG"), ("at", "IN"), ("10", "CD"), ("%", "NN"), (".", ".")]
# run the chunker on this input
print cp.parse(sentence)