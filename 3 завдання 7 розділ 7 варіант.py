import nltk
sentence = [("A", "DT"), ("white", "JJ"), ("light", "JJ"), ("bus", "NN"), ("came", "VBD"), ("to", "IN"), ("a", "DT"), ("stopt", "NN"), ("in", "IN"), ("front", "NN"), ("of", "IN"), ("the", "DT"), ("Flynn-Fletcher", "JJ"), ("residence", "NN"), ("that", "WDT"), ("same", "JJ"), ("evening", "NN"), (",", ","), ("in", "IN"), ("another", "DT"), ("demension", "NN"), (".", ".")]
grammar = r"NP:  {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()
