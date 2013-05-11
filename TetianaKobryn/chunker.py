# TODO
# Write a tag pattern ...
# Add these patterns  to the grammar, one per line.
# 
#
#
#
# Presented by Tetiana Kobryn

# Chapter 7, Ex.5
# Write a tag pattern to cover noun phrases that contain gerunds, e.g., the/DT
# receiving/VBG end/NN, assistant/NN managing/VBG editor/NN. Add these patterns
# to the grammar, one per line. Test your work using some tagged sentences of
# your own devising.



import nltk
from nltk.corpus import conll2000
#defining a  grammar with a regular expression rules
grammar = r"""
    NP: {<DT|NN.?>*<VBG><NN>}
        {<DT>?<JJ>*<NN.?>+}  
"""

#creating a chunk parser
new_chunk = nltk.RegexpParser(grammar)
#some example phrases
phrase1 = [("The", "DT"), ("receiving", "VBG"), ("end", "NN")]
phrase2 = [("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]

#testing a grammar on some phrases
result1 = new_chunk.parse(phrase1)
print result1
result2 = new_chunk.parse(phrase2)
print result2

#evaluating created chunker on chunked sentences from conll2000 corpus
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print new_chunk.evaluate(test_sents)
