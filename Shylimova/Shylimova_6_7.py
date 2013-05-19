# Shylimova K. Al-13
# Chapter 6 task 7
# Метод класифікації з врахуванням класу та пунктуації попереднього повідомлення
# виявився точнішим.

import nltk
def standart_method(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features

def prev_class_method(post,i,history):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
        if i:
            features["prev-class"] = history[i-1]["class"]
            features["prev-punct"] = history[i-1]["punctuation"]
        features["punct"] = post[-1]
    return features

posts = nltk.corpus.nps_chat.xml_posts()
history=[]
featuresets = []
for post in posts: 
    featuresets.append((standart_method(post.text), post.get('class')))
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
standart_classifier = nltk.NaiveBayesClassifier.train(train_set)

featuresets = []
for i, post in enumerate(posts):
    featuresets.append((prev_class_method(post.text, i, history), post.get('class')))
    history.append({"class": post.get('class'),
                    "punctuation": post.text[-1]})
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
modified_classifier = nltk.NaiveBayesClassifier.train(train_set)

print "Standart method accuracy: ", nltk.classify.accuracy(standart_classifier, test_set)
print "Modified method accuracy: ", nltk.classify.accuracy(modified_classifier, test_set)
