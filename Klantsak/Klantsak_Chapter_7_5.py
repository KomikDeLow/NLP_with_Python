# Veronika KLantsak ALs-11

import nltk
grammar = """ # stvorutu chunk gramatuky
NP: {<DT>?<VBG>*<NN>}
{<DT>?<VBG>*<NNS>}
{<DT>?<NN>*<VBG>}
{<NN>?<VBG>*<NN>}
"""
# vukorustovyyuchu cyu gramatuky stvoryyu chunk parser
cp = nltk.RegexpParser(grammar)
# vuznachayu rechennya z gerundiem dlya chankingy
sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"), ("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
# zapyskayu chanker
print cp.parse(sentence)
# define a sentence of my own to be chunked
sentence = [("Oksana", "NNP"), ("wrote", "VBD"), ("the", "DT"), ("letter", "NN"), ("in", "IN"), ("the", "DT"), ("room", "NN"), (".", "."), ("The", "DT"), ("following", "VBG"), ("sentences", "NNS"), ("concern", "VB"), ("the", "DT"), ("issue", "NN"), (".", "."), ("The", "DT"), ("growing", "VBG"), ("thread", "NNS"), ("disappeared", "VBD"), (".", "."), ("The", "DT"), ("price", "NN"), ("cutting", "VBG"), ("at", "IN"), ("18", "CD"), ("%", "NN"), (".", ".")]
# zapyskayu chanker
print cp.parse(sentence)
