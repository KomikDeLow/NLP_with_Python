#TODO
# How does your program classify dialogue acts
#
# Presented by Tetiana Kobryn

# Chapter 6, Ex.7
# The dialogue act classifier assigns labels to individual posts, without considering
# the context in which the post is found. However, dialogue acts are highly dependent
# on context, and some sequences of dialogue act are much more likely than
# others. For example, a ynQuestion dialogue act is much more likely to be answered
# by a yanswer than by a greeting. Make use of this fact to build a consecutive classifier
# for labeling dialogue acts. Be sure to consider what features might be useful.
# See the code for the consecutive classifier for part-of-speech tags in Example 6-5
# to get some ideas.

"""This dialogue act classifier assigns labels to individual posts with considering
the context in which the post is found. Type of previous message is taking into account."""

import nltk
posts = nltk.corpus.nps_chat.xml_posts()
previous_post=[] # here the type of previous message will be saved
# function for getting features from message
def dialogue_act_features(post,i,previous_post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
        if i == 0:
            features["prev-class"] = ""
        else:
            features["prev-class"] = previous_post[i-1]
            # type of previous message
        return features
featuresets=[]
for i, post in enumerate(posts): 
    featuresets.append((dialogue_act_features(post.text, i, previous_post),
                        post.get('class')))
    previous_post.append(post.get('class')) 
size = int(len(featuresets) * 0.1)
# Splitting data to training and test set
train_set, test_set = featuresets[size:], featuresets[:size]
# Building a classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
# Evaluating accuracy
print "Accuracy of the classifier:"
print nltk.classify.accuracy(classifier, test_set)
# Showing most informative features of the classifier
classifier.show_most_informative_features(5)

