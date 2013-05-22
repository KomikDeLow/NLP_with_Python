#Iryna Ros, PRLs-11, chapter 6, exersise 7
#
#We build a consecutive claaifier for labeling dialogue acts.
#In this program we assign labels to individual posts with considering context.
#We use  ClassOfPost for classification of user posts.
#
import nltk
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
print nltk.classify.accuracy(classifier, test_set)
            
def ClassOfPost(PreviousClass, word):
    print classifier.classify({ 'prev-class': PreviousClass, 'contains(%s)' % word.lower() : True})
