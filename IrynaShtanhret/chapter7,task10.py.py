#Iryna Shtanhret, AL-13, Task 10, CHapter 7
#The bigram chunker scores about 90% accuracy. Study its errors and try to work
#out why it doesn’t get 100% accuracy. Experiment with trigram chunking. Are you
#able to improve the performance any more?
import nltk
import nltk.chunk#importing a chunk corpus and we can evaluate chunkers
from nltk.corpus import conll2000
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)
#in the result a tagger didn't find any chunks

grammar = r"NP: {<[CDJNP].*>+}"#looking for tags beginning with letters that are characteristic of noun phrase tags 
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
#the result is better
class BigramChunker(nltk.ChunkParserI):#Having built a unigram chunker, it is quite easy to build a bigram chunker: we simply change the class name to BigramChunker
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramChunker(train_data) 

    def parse(self, sentence): 
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  

bigram_chunker = BigramChunker(train_sents)
print bigram_chunker.evaluate(test_sents)             
#by trying adding different features to the feature extractor function we see that we can further improve the performance of the NP chunker.	