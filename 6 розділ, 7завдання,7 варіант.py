      
>>> import nltk
>>> posts = nltk.corpus.nps_chat.xml_posts()
>>> history=[]
>>> def dialogue_act_features(post,i,history):
  features = {}
	for word in nltk.word_tokenize(post):
		features['contain(%s)' % word.lower()] = True
		if i == 0:
			features["prev-class"] = ""
		    else:
                        features["prev-class"] = hisrory[i-1]
                return features
>>> featureset=[]
>>> for i, post in enumerate(posts) :
	featuresets.append((dialogue_act_features(post.text, i, hitory), post.get('class')))
	history.append(post.get('class'))
>>> size = int (len(features) * 0.1)
>>> train_set,test_set = featureset[size:], featuresets[:size]
>>> classifier = nltk.NaiveBayesClassifier.train(train_set)
>>> print nltk.classify.accuracy(classifier, test_set)
0.644886363636
