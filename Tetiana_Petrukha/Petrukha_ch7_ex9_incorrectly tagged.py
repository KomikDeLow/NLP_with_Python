# TODO
# example sentence is not correctly chunked
# Look for other  examples of correctly chunked noun phrases with incorrect tags.
#
# Petrukha Tetiana Als-11
# Chapter_7, Ex_9

# Sometimes a word is incorrectly tagged, e.g., the head noun in 12/CD or/CC so/
# RB cases/VBZ. Instead of requiring manual correction of tagger output, good
# chunkers are able to work with the erroneous output of taggers. Look for other
# examples of correctly chunked noun phrases with incorrect tags.

import nltk, re, pprint
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) # default sentence segmenter
    sentences = [nltk.word_tokenize(sent) for sent in sentences] # word tokenizer
    sentences = [nltk.pos_tag(sent) for sent in sentences] # part-of-speech tagger
# This function takes raw text and chops and then connects the process to break
# it down into sentences, then words and then complete part-of-speech tagging
    print sentences # print sentences

    
document = "Please, book me a room in this hotel "
print ie_preprocess(document)
grammar = r"""
NP: {<DT|JJ|NN.*>+}           # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>}                # Chunk prepositions followed by NP
VP: {<VB.*><NP|PP|CLAUSE>+$}  # Chunk verbs and their arguments
CLAUSE: {<NP><VP>}            # Chunk NP, VP
"""
sentence = [('Please', 'NN'), (',', ','), ('book', 'NN'), ('me', 'PRP'), ('a', 'DT'),('room', 'NN'),
            ('in', 'IN'), ('this', 'DT'), ('hotel', 'NN')] # create sentence with POS tags
cp = nltk.RegexpParser(grammar) # create a chunk parser
result = cp.parse(sentence) # test a chunk parser on my example sentence
print result  # print result
