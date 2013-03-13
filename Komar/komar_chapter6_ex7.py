import nltk
posts = nltk.corpus.nps_chat.xml_posts()
komar=[]
def pos_features(post,i,komar):
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
		if i == 0:
			features["prev-class"] = "<START>"
		else:
			features["prev-class"] = komar[i-1]
		return features

feature_sets=[]
for i, post in enumerate(posts):
        feature_sets.append((pos_features(post.text, i, komar), post.get('class')))
        komar.append(post.get('class'))

        
size=int(len(feature_sets)*0.1)
train_set, test_set = feature_sets[size:], feature_sets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
