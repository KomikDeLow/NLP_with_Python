#Pokladok Oksana
import nltk
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
word_tag_pairs = nltk.bigrams(brown_news_tagged)
print list(nltk.FreqDist(t[1] for (t, r) in word_tag_pairs if r[1] == 'N'))

# In the following code sample, we train a unigram tagger, use it to tag a sentence, and then evaluate:
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
# We should split the data, training on 90% and testing on the remaining 10%:
size = int(len(brown_tagged_sents) * 0.9) 
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.tag(brown_sents[2007]) # First we train it, then use it to tag untagged sentences


unseen_sent = brown_sents[4203]
print bigram_tagger.tag(unseen_sent)
print bigram_tagger.evaluate(test_sents)
"""Its overall accuracy score is very low"""