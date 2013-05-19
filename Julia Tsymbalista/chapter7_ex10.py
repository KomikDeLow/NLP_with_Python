# Presented by Iuliia Tsymbalista
#chapter 7, ex.10


import nltk
import nltk.chunk
from nltk.corpus import conll2000
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
grammar = r"NP: {<[CDJNP].*>+}" # the noun phrase based on the regular expression 
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)

#The constructor expects a list of training sentences.
#It first converts training data to a form that’s suitable for training the tagger,
#using tree2conlltags to map each chunk tree to a list of word,tag,chunk triples. It then
#uses that converted training data to train a unigram tagger, and stores it in self.tag
#ger for later use.
class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramChunker(train_data)

   # the parse method for chunking new sentences
    def parse(self, sentence): 
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  

#having BigramChunker, we can train it using the CoNLL-2000 Chunking
#Corpus, and test its resulting performance:
test_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])


