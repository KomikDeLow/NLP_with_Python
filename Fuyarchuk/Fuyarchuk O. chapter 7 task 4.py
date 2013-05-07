# TODO
# "Determine which  tags  (or  tag sequences) are most  likely  to make up
# chinks with  the help of your own utility program.
# Compare the performance and simplicity of this approach relative to a
# chunker based entirely on chunk rules."
#
#


# Fuyarchuk O. Chapter 7 Task 4
import nltk
grammar= r"""
	Np:
	  {<.*>+}                               #chunk everything
	  }<VB. |IN>+{                          #chink sequences of VB and IN
	  """
sentence=[("The", "DT"), ("capable", "JJ"), ("agile", "JJ"), ("boy", "NN"),
          ("worked", "VBD"), ("at", "IN"),  ("the", "DT"), ("garden", "NN")]
cp=nltk.RegexpParser(grammar)## using grammar create a chunk parser and test
                             #it on our sentence
from nltk.corpus import conll2000 # import conll2000 corpus
cp=nltk.RegexpParser(grammar)# using grammar create a chunk parser and test
                             #it on our sentence
test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=('NP',))
print cp.evaluate(test_sents)# print evaluation result
