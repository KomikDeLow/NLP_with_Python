#Irena Marunyshyn PRLs-12 Chapter5 Ex32
import nltk
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=90, max_rules=100,  min_score=4, trace=7, train=0.9)
nltk.tag.brill.demo(num_sents=100, max_rules=100, min_score=4, trace=7, train=0.7)
nltk.tag.brill.demo(num_sents=300, max_rules=100, min_score=4, trace=7, train=1)
nltk.tag.brill.demo(num_sents=500, max_rules=100, min_score=4, trace=7, train=1.1)
nltk.tag.brill.demo(num_sents=1000, max_rules=100,min_score=4, trace=7, train=1.5)
