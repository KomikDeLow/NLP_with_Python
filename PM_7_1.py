import nltk
text='''
We PRP B-NP
saw VBD O
the DT B-NP
little JJ I-NP
dog NN I-NP
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()
text='''
dog NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()

# The most widespread file representation uses IOB tags. In this scheme, each token is tagged with one of three special
# chunk tags, I (inside), O (outside), or B (begin). A token is tagged as B if it marks the
# beginning of a chunk. Subsequent tokens within the chunk are tagged I. All other
# tokens are tagged O. The B and I tags are suffixed with the chunk type, e.g., B-NP, INP.
# Of course, it is not necessary to specify a chunk type for tokens that appear outside
# a chunk, so these are just labeled O.
