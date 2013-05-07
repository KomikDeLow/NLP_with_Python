import nltk
from nltk.corpus import brown
sent1=nltk.word_tokenize("Go away!") #After I have done tokenization of the first sentence
nltk.pos_tag(sent1) #python defined that GO in Go away sentence is a noun
                    #It's a wrong statement, cause Go is a verb
sent2=nltk.word_tokenize("We went on the excursion.") #After tokenizing second sentence
nltk.pos_tag(sent2) # result is that went is a verb in past tence
print nltk.pos_tag(sent1)
print nltk.pos_tag(sent2)

