# Iuliia Tsymbalista
# chapter 5 ex.30
# task:
#Preprocess the Brown News data by replacing low-frequency words with UNK,
#but leaving the tags untouched. Now train and evaluate a bigram tagger on this
#data. How much does this help? What is the contribution of the unigram tagger
#and default tagger now?


# Also I have used TrigramTagger for evaluation. 


import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
vocab = nltk.FreqDist(brown.words(categories='news'))

# Replacing all word with freq. <= 2 to "UNK"
mapping = nltk.defaultdict(lambda: 'UNK')
for v,t in brown.tagged_words(categories='news'):
    if vocab[v]>2:
        mapping[v],t = v,t
        
# Saving results in list new_tagged_sents 
new_tagged_sents=[]
for i in brown.tagged_sents(categories='news'):
    new_tagged_sents.append([(mapping[v],t) for (v,t) in i])



# build train sents and evaluate them with Default, Unigram and Bigram tagger
size = int(len(brown_tagged_sents) * 0.9)
train_sents1 = brown_tagged_sents[:size]
test_sents1 = brown_tagged_sents[size:]
train_sents2 = new_tagged_sents[:size]
test_sents2 = new_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents1, backoff=t0)
t2 = nltk.BigramTagger(train_sents1, backoff=t1)
print t2.evaluate(test_sents1)

t1 = nltk.UnigramTagger(train_sents2, backoff=t0)
t2 = nltk.BigramTagger(train_sents2, backoff=t1)
print t2.evaluate(test_sents2)

t2 = nltk.BigramTagger(train_sents2, backoff=t0)
print t2.evaluate(test_sents2)

# evaluate sentences with trigram tagger
t2= nltk.TrigramTagger(train_sents2, backoff=t0)
print t2.evaluate(test_sents2)

# I have found that the accuracy is lower when we use trigram tagger

