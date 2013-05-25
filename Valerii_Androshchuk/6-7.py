# Valerii Androshchuk APL(s)-13.
# Chapter 6, Task 7.
# Built a consecutive classifier for labeling dialogue acts.

import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[] 
# Dialogues and backup data.

def dialogue_act_features(post,i,history):
# Searching data.
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains(%s)' % word.lower()] = True
            if i == 0:
                features["prev-class"] = ""
            else:
                features["prev-class"] = history[i-1]
        return features
featuresets=[]

for i, post in enumerate(posts): 
        featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
        history.append(post.get('class'))
# Data processing.

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print test_set [:1]
# Displaying results. Quantity can be changed optionally.
print nltk.classify.accuracy(classifier, test_set)
# Dispaying accuracy.






