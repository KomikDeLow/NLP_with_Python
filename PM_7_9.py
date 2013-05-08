import nltk
# create a multistage chunk grammar
grammar = r"""
NP: {<DT|JJ|NN.*>+}
PP: {<IN><NP>}
VP: {<VB.*><NP|PP|CLAUSE>+$}
CLAUSE: {<NP><VP>}
"""
# using this grammar, create a chunk parser
cp = nltk.RegexpParser(grammar)
# define a sentence to be chunked
sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
# run the chunker on this input
print cp.parse(sentence)
# unfortunately this result misses the VP headed by saw, so add an optional second argument loop to specify the number of times the set of patterns should be run
cp = nltk.RegexpParser(grammar, loop=2)
print cp.parse(sentence)

