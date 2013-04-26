## Nataliia Kozachuk, Prls-12, Chapter 7_Ex10. 
import nltk
from nltk.corpus import conll2000 ##acces the data in Chunking corpus
cp = nltk.RegexpParser("") ## stvoryemo RegexpParser text
#( RegexpParser works by defining rules for grouping different words together)

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
#get training and testing data
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar) ## use the above mentioned  grammar
print cp.evaluate(test_sents)#the chunker got decent results and is ready to use

class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):  
## build a chunker using a unigram tagger
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramChunker(train_data) 
#we are trying to determin the correct chunk tag, given each words part-of speech tag

    def parse(self, sentence): 
##  to parse a sentence. Takes a sentence as a list of words
       
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
bigram_chunker = BigramChunker(train_sents)
## 
