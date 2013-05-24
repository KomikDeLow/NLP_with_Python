import nltk
text='''  # I add text
We PRP B-NP
saw VBD O
the DT B-NP
angry JJ I-NP
dog NN I-NP
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw() # we are building tree representation
text='''
dog NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()# we are building tree representation
# In the most widespread file representation are used IOB tags.
# In such scheme each token is tagged.
# Of course, it is not necessary to specify a chunk type for tokens that appear outside a chunk
