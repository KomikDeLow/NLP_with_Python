#Nataliia Kozachuk PRLs-12 Chapter6 Ex. 7
import nltk
posts = nltk.corpus.nps_chat.xml_posts()# vuluchaemo golovni dani z korpusu NPS_Chat
history = []
def dialogue_act_features(post,i,history):# we use a feature extractor
	features = {} # vuznachaemo  feature extractor
	for word in nltk.word_tokenize(post):
		features['contains(%s)'% word.lower()] = True# robumo perevirky wob vuznachutu jaki slova mistut' povidomlennja
		if i ==0:
			features["prev-class"]=""
			
		else:
			features["prev-class"]= history[i-1]
		return features

	
featuresets = []# we use a  features classifier
for i, post in enumerate(posts):# pronumerovanuj spusok povidomlenj
	featuresets.append((dialogue_act_features(post.text,i,history), post.get('class')))
	history.append(post.get('class'))#perelik ysih tupiv povidomlenj

	
size = int(len(featuresets)*0.1)# vkazyemo rozmir danuh dlja testyvannja
train_set, test_set = featuresets[size:], featuresets[:size]# rosdiljaemo dani
classifier = nltk.NaiveBayesClassifier.train(train_set)# stvoryemo i vukorustovyemo Classifier
print nltk.classify.accuracy(classifier, test_set)# ocinyeno tochnist nawogo texty

