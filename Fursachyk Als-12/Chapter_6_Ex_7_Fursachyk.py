#Chapter_6_Ex_7_Fursachyk
import nltk
posts = nltk.corpus.nps_chat.xml_posts()#golovni dani z korpusu NPS_Chat
history = []
def dialogue_act_features(post,i,history):# vykorystovuemo funkciju dlya poshuku danyh
	features = {} 
	for word in nltk.word_tokenize(post):
		features['contains(%s)'% word.lower()] = True #perevirka dlya vuznachennya sliv yaki mistut' povidomlennja
		if i ==0:
			features["prev-class"]=""
			
		else:
			features["prev-class"]= history[i-1]
		return features

	
featuresets = []
for i, post in enumerate(posts):# funkciya obrobky pronumerovanogo spysku povidomlen'
	featuresets.append((dialogue_act_features(post.text,i,history), post.get('class')))
	history.append(post.get('class'))#perelik ysih tupiv povidomlen'

	
size = int(len(featuresets)*0.1)# vkazuemo rozmir danyh dlja testuvannya
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)# stvoryemo klasyfikator
print nltk.classify.accuracy(classifier, test_set)# ocinyuemo tochnis't' textu

