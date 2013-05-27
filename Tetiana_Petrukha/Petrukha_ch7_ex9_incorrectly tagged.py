# fine
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

    
document = "Tall beautiful girls lay on the beach and look on the blue sky"
print ie_preprocess(document)
grammar = """
         NP:
         {<DT>?<JJ>*<NN>*<NNS>*}
         }<VBP|IN>+{
         """
sentence= [('Tall', 'JJ'), ('beautiful', 'JJ'), ('girls', 'NNS'), ('lay', 'VBP'), ('on', 'IN'),
           ('the', 'DT'), ('beach', 'NN'), ('and', 'CC'), ('look', 'VBP'), ('on', 'IN'),
           ('the', 'DT'), ('blue', 'JJ'), ('sky', 'NN')] # create sentence with POS tags
cp = nltk.RegexpParser(grammar) # create a chunk parser
result = cp.parse(sentence) # test a chunk parser on my example sentence
print result  # print result
