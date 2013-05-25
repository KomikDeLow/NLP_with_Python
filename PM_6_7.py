import nltk
# call xml_posts() to get a data structure representing the XML annotation for each post
posts=nltk.corpus.nps_chat.xml_posts()[:100]
# define a simple feature extractor that checks what words the post contains
def dialogue_act_features(post):
	features={}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()]=True
		return features
# construct the training and testing data by applying the feature extractor toeach post using post.get('class') to get a post’s dialogue act type
featuresets=[(dialogue_act_features(post.text), post.get('class')) for post in posts]
size=int(len(featuresets)*0.1)
train_set, test_set=featuresets[size:], featuresets[:size]
# create a new classifier
classifier=nltk.NaiveBayesClassifier.train(train_set)
# calculate the accuracy of a classifier model on a given test set
print nltk.classify.accuracy(classifier, test_set)
