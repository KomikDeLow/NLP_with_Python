# TODO
# I was seeing this program many times...
#

# Irena Marunyshyn PRLs-12 Chapter6 Ex8
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category)##this pairs the words in each doc, with the pos/neg category
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)[:100]]

random.shuffle(documents)# using true or false
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_words)# y texti e 39768 sliv
word_features = all_words.keys()[:200]# feature extractor
def document_features(document):# searching for owr words( chacks whether owr words are included)
	document_words = set(document)
	features = {}
	for word in word_features:
		 features['contains(%s)' % word] = (word in document_words)
	return features

featuresets = [(document_features(d),c) for (d,c) in documents]
train_set, test_set = featuresets[90:], featuresets[:30]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)# chastota sliv dorivnye 0.7
for word in all_words.keys()[:300]:# rozhuruemo nawy programu z yrachyvannjam hypernyms
	 if all_words[word] < all_words[all_words.keys()[200]]:
		  for synset in wn.synsets(word):
			  for hypernyms in synset.hypernyms():
				  for l_names in hypernyms.lemma_names:
					  if l_names in all_words.keys()[:200]:
						  if word not in word_features:
							   word_features.append(word)

							   

print len(word_features)# dovzhuna heponimiv rozwurulasja na 238 sliv
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[90:], featuresets[:30]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)# chastota dorivnye o.76
# za dopomogoy danoi programu mu mozhemo vuznachatu chastoty sliv y texti, a takozh
# rozhuruvatu ci slova z vukorustannjam hiperonimiv abo heponimiv i znaidemo
# ix chastoty y danomy texti. Mu takozh mozhemo znaitu chastoty sliv z wurwum znachennjam
# tobto nazvy klasy, rodove ponjattja(oznaku) i vyzjke znachennja- element klasy, vlastuvistj.
# For example: animal- dog - bulldog. mu zmozhemo krawe analizyvatu text.
