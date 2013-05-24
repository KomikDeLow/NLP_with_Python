
# Veronika Klantsak Als-11
>>> >>> import nltk
>>>posts = nltk.corpus.nps_chat.xml_posts()
>>>history=[] # zminna dkya zberezhennya tupy poperdnjogo povidomlennya(post�s dialogue act type)
# fynkciya dlya vlychennhya vlastuvostej(oznak) z povidomlennya
>>>def dialogue_act_features(post,i,history):
features = {}
for word in nltk.word_tokenize(post):
features['contains(%s)' % word.lower()] = True
if i == 0:
features["prev-class"] = ""
else:
features["prev-class"] = history[i-1]# tup poperednjogo povidomlennya
return features
>>>featuresets=[]
>>>for i, post in enumerate(posts): # obroblyaemo pronymerovanui spusok povidomlenn'
featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
history.append(post.get('class')) # spusok tupiv vsix povidomlenn'
>>>size = int(len(featuresets) * 0.1)
>>> train_set, test_set = featuresets[size:], featuresets[:size]
>>>classifier = nltk.NaiveBayesClassifier.train(train_set)
>>> print nltk.classify.accuracy(classifier, test_set)
0.644886363636
