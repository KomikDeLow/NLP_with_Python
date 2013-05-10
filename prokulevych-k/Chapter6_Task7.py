# fine
#

#Прокулевич К. ПРЛс-11, Розділ6, Задача 7
#building a consecutive classifier for labeling dialogue acts
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[]
 def pos_features(post,i,history): #augment feature extractor function to take a history argument
	features = {}  # create obtaining features' function
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True # check which words contains the post 
		if i == 0:
			features["prev-class"] = "<START>"
		else:
			features["prev-class"] = history[i-1] # obtaining class of the previous post from list "history"
		return features

featuresets=[] # create an empty list for features
for i, post in enumerate(posts): 
	featuresets.append((pos_features(post.text, i, history), post.get('class')))
	history.append(post.get('class')) # append list of all types of posts


size=int(len(featuresets)*0.1) # choose data size for testing
train_set, test_set = featuresets[size:], featuresets[:size] 
classifier = nltk.NaiveBayesClassifier.train(train_set) # create a classifier
print nltk.classify.accuracy(classifier, test_set) # evaluate the accuracy of the work
