# fine
#
# TODO
# Comments?

# Petrukha Tetiana Als-11
# Chapter_6, ex_7

# The dialogue act classifier assigns labels to individual posts, without considering
# the context in which the post is found. However, dialogue acts are highly dependent
# on context, and some sequences of dialogue act are much more likely than others.
# For example, a ynQuestion dialogue act is much more likely to be answered by a yanswer
# than by a greeting. Make use of this fact to build a consecutive classifier
# for labeling dialogue acts. Be sure to consider what features might be useful.
# See the code for the consecutive classifier for part-of-speech tags in Example 6-5
# to get some ideas.


import nltk
posts = nltk.corpus.nps_chat.xml_posts() # importing posts
history=[]
def pos_features(post,i,history):
	features = {}  # creating function of obtaining features
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True # check what words the post contains
		if i == 0:
			features["prev-class"] = "<START>"
		else:
			features["prev-class"] = history[i-1] # obtaining class of the previous post from list "history"
		return features
	    
featuresets=[] # creating an empty list for the features
for i, post in enumerate(posts): # a cycle running throught the posts and appendind the features
        featuresets.append((pos_features(post.text, i, history), post.get('class')))
        history.append(post.get('class')) # append list of all types of posts

size=int(len(featuresets)*0.1) # choose data size for testing
train_set, test_set = featuresets[size:], featuresets[:size] # divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set) # create a classifier
print nltk.classify.accuracy(classifier, test_set) # evaluate the accuracy of the work
