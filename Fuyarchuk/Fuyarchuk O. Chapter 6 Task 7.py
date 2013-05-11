import nltk
posts=nltk.corpus.nps_chat.xml_posts() 
history=[] # змінна для зереження типу попереднього повідомлення 
def dialogue_act_features(post,i,history):# функція для вилучення ознак повідомлення
	features={}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' %word.lower()]=True
		if i==0:
			features["prev-class"]=""
		else:
			features["prev-class"]=history[i-1]# тип попереднього повідомлення
		return features

featuresets=[]
for i,post in enumerate(posts): # обробка пронумерованого списоку повідомлень
	featuresets.append((dialogue_act_features(post.text,i,history),post.get('class')))
	history.append(post.get('class')) # список типів всіх повідомлень
size=int(len(featuresets)*0.1)
train_set, test_set=featuresets[size:],featuresets[:size]
classifier=nltk.NaiveBayesClassifier.train(train_set) 
print nltk.classify.accuracy(classifier, test_set)# визначення точності роботи класифікатора
