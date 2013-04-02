# TODO
# It isn't the Python modul
#
#

>>> import nltk
>>> grammar = r"""
  NP: {<DT|NN>?<VBG><NN>}"""
>>> sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"),(",", ","),
("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
>>> cp = nltk.RegexpParser(grammar)
>>> print cp.parse(sentence)
(S
  (NP the/DT receiving/VBG end/NN)
  ,/,
  (NP assistant/NN managing/VBG editor/NN))
>>>
