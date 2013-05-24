Chapter 6 ex. 7

import nltk
posts=nltk.corpus.nps_chat.xml_posts()
history=[] # A variable to save the type of previous message
 def dialogue_act_features(post,i,history): # deleting message features
	features={}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' %word.lower()]=True
		if i==0:
			features["prev-class"]=""
		else:
			features["prev-class"]=history[i-1] # type of previous message
		return features

	
 featuresets=[]
   for i,post in enumerate(posts): # creating the enumerated message list
	featuresets.append((dialogue_act_features(post.text,i,history),post.get('class')))
	history.append(post.get('class'))

 size=int(len(featuresets)*0.1)
 train_set, test_set=featuresets[size:],featuresets[:size] # creatinf two data sets
 classifier=nltk.NaiveBayesClassifier.train(train_set)  # Training the classifier
 print nltk.classify.accuracy(classifier, test_set) #Evaluating the accuracy of the classifier  
