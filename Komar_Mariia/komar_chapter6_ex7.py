# Komar Mariia Als-11
# Chapter_6, Ex_7

#The dialogue act classifier assigns labels to individual posts, without considering
#the context in which the post is found. However, dialogue acts are highly dependent
#on context, and some sequences of dialogue act are much more likely than
#others. For example, a ynQuestion dialogue act is much more likely to be answered
#by a yanswer than by a greeting. Make use of this fact to build a consecutive classifier
#for labeling dialogue acts. Be sure to consider what features might be useful.
#See the code for the consecutive classifier for part-of-speech tags in Example 6-5
#to get some ideas.
#
import nltk
posts = nltk.corpus.nps_chat.xml_posts() #extract the basic messaging data from NPS Chat Corpus
history=[]
def pos_features(post,i,history):
	features = {} # define a simple feature extractor
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True #check what words the post contains
		if i == 0:
			features["prev-class"] = "<START>"
		else:
			features["prev-class"] = history[i-1]
		return features

feature_sets=[]
for i, post in enumerate(posts): # process numbered list of posts
        feature_sets.append((pos_features(post.text, i, history), post.get('class')))
        history.append(post.get('class')) # append list of all types of posts

        
size=int(len(feature_sets)*0.1) #choose data size for testing
train_set, test_set = feature_sets[size:], feature_sets[:size] #divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set) #create a classifier
print nltk.classify.accuracy(classifier, test_set) #evaluate the accuracy of the work
