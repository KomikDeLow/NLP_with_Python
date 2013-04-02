# fine
#

# Dialog class identifier that uses not only the featuring words of diferrent posts
# but also the class of the previous post
import nltk
posts = nltk.corpus.nps_chat.xml_posts() # importing posts
history=[]

def dialogue_act_features(post,i,history): # creating function of obtaining features
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
		if i == 0:
			features["prev-class"] = ""
		else:
			features["prev-class"] = history[i-1] # obtaining class of the previous post from list "history"
	return features

featuresets=[] # creating an empty list for the features of posts
for i, post in enumerate(posts): # a cycle running throught the posts and appendind the features
	featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
	history.append(post.get('class')) # appendid classes of all posts

train_set, test_set = featuresets[1:9000], featuresets[9000:] # dividing test and train data, not using the 1-st post
  # becouse it doesn't have a "prev-class" parameter
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'train set items =', len(train_set),' test set items =', len(test_set) # giving the numbers of used data entries for the test and train data
print 'Accuraci', (nltk.classify.accuracy(classifier, test_set)*100.0),'%' # establishing the accuracy of the tagger
