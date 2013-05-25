# by Ivanna Kushniruk
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
prepost=[] # class of previous post will be here
""" function extracts features. if it is 1rst post (i==0), there is no previous
post, so feature of previous post is nothing, next posts are labeled according to
previous post and returns feature, imho - class or type of post,i.e. if previous post
was question, next might be answer"""
def dialogue_act_features(post,i,prepost):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
        if i == 0:
            features["prev-class"] = ""
        else:
            features["prev-class"] = prepost[i-1]
        return features
featuresets=[]
for i, post in enumerate(posts): 
    featuresets.append((dialogue_act_features(post.text, i, prepost),
                        post.get('class')))
    prepost.append(post.get('class')) 
size = int(len(featuresets) * 0.1)
# organisation of training and testing data according to size
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set) # building classifire
print nltk.classify.accuracy(classifier, test_set) #shows accuracy
            

