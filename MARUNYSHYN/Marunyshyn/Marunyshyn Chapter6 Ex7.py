# fine
# але прочитайте будь-ласка Ch4.
#


#Irena Marunyshyn PRLs-12 Chapter6 Ex. 7
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history = []
def dialogue_act_features(post,i,hiatory):# feature extractor
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)'% word.lower()] = True
		if i ==0:
			features["prev-class"]=""
			
		else:
			features["prev-class"]= history[i-1]
		return features

	
featuresets = []# features classifier
for i, post in enumerate(posts):
	featuresets.append((dialogue_act_features(post.text,i,history), post.get('class')))
	history.append(post.get('class'))

	
size = int(len(featuresets)*0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)# train a model using the training set
print nltk.classify.accuracy(classifier, test_set)# then run it on the test set
# with the help of this programm we can see the accuracy of our text.and we can
# evaluate the classifier on a large quantity of data.
