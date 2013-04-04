#Irena Marunyshyn PRLs-12 Chapter5 Ex32
import nltk
help(nltk.tag.brill.demo)#Brill's transformational rule-based tagger.
nltk.tag.brill.demo(num_sents=90, max_rules=100,  min_score=4, trace=7, train=0.9)#Brill Tagger Demonstration
nltk.tag.brill.demo(num_sents=100, max_rules=100, min_score=4, trace=7, train=0.7)
nltk.tag.brill.demo(num_sents=300, max_rules=100, min_score=4, trace=7, train=1)
nltk.tag.brill.demo(num_sents=500, max_rules=100, min_score=4, trace=7, train=1.1)
nltk.tag.brill.demo(num_sents=1000, max_rules=100,min_score=4, trace=7, train=1.5)# in this program we are finding  how many sentences of training and testing data to use,
#maximum number of rule instances to create and
#the minimum score for a rule in order for it to be considered
#the fraction of the the corpus to be used for training (1=all)
#the level of diagnostic tracing output to produce (0-4)
#so in this program we are finding Brill accuracy , the rules and errors.
