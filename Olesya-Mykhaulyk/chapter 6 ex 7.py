#Olesya Mykhaulyk
#ALs-12
#chapter 6 ex 7
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
store=[] # I'm going to use this variable in order to store post’s dialogue act type
def dialogue_act_features(post,i,store): #function used in order to cut features from the message
    features = {}
for word in nltk.word_tokenize(post):
    features['contains(%s)' % word.lower()] = True
    if i == 0:
        features["prev-class"] = ""
    else:
        features["prev-class"] = store[i-1] #previous message type
return features
featuresets=[]
for i, post in enumerate(posts): # processing the numbered list of reports
    featuresets.append((dialogue_act_features(post.text, i, store), post.get('class')))
store.append(post.get('class')) #the list of all messages' types
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)# evaluation of the classifier 
