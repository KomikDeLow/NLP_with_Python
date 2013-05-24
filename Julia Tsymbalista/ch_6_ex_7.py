
# Iuliia Tsymbalista
# Chapter 6.7
# Classifier of dialogue acts with considering the context.
# This program assigns labels to individual posts with considering context.



import nltk
from nltk import all
posts = nltk.corpus.nps_chat.xml_posts()
history=[]

def dialogue_act_features(post,i,history):
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

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'example from test_set', test_set [:5]
print 'Accuracy: %4.2f' % nltk.classify.accuracy(classifier, test_set)






