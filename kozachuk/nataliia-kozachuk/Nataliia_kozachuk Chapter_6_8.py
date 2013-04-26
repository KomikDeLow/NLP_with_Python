# Nataliia Kozachuk PRLs-12 Chapter6_8
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category)##Make a randomized list of pairs, words and category, for each fileid
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)[:100]]

random.shuffle(documents)# shuffle
### Get a frequency distribution of all words, and pick the first 200.
# The items in the frequency distribution are label-value pairs, where
# the label is a word and the value is its count.  All we are doing here
# is reducing the number of features.
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_words)#  39768 words
word_features = all_words.keys()[:200]# feature extractor
### Function to create a document feature list.  For each document, for each of
# our 200 words, we have a feature which is the word and "true" or "false"
def document_features(document):
        document_words = set(document)
	features = {}
	for word in word_features:
		 features['contains(%s)' % word] = (word in document_words)
	return features
# we  call the function.
featuresets = [(document_features(d),c) for (d,c) in documents]
# Create our training and test sets, run the classifier
train_set, test_set = featuresets[90:], featuresets[:30]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)# accuracy=0.7
for word in all_words.keys()[:300]:
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
