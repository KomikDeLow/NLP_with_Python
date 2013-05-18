#Khrystyna Hensirovska ALs-12 Chapter6 task 7
#The dialogue act classifier assigns labels to individual posts, without considering
#the context in which the post is found. However, dialogue acts are highly dependent
#on context, and some sequences of dialogue act are much more likely than
#others. For example, a ynQuestion dialogue act is much more likely to be answered
#by a yanswer than by a greeting. Make use of this fact to build a consecutive classifier
#for labeling dialogue acts. Be sure to consider what features might be useful.
#See the code for the consecutive classifier for part-of-speech tags in Example 6-5
#to get some ideas.
import nltk
#Викликаємо процедуру xml_posts()щоб отримати структуру даних,що представляють
#собою коментарі XML для кожного повідомлення
posts = nltk.corpus.nps_chat.xml_posts()
history = []
#Визначаємо простий fearute extractor,який перевіряє які слова містяться в
#повідомленні
def dialogue_act_features(post,i,history):
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)'% word.lower()] = True
		if i ==0:
			features["prev-class"]=""
			
		else:
			features["prev-class"]= history[i-1]
		return features
#Будуємо дані для тестування і тренування застосовуючи feature extractor
#для кожного повідомлення і створюємо новий класифікатор
	
featuresets = []
for i, post in enumerate(posts):
	featuresets.append((dialogue_act_features(post.text,i,history), post.get('class')))
	history.append(post.get('class'))

	
size = int(len(featuresets)*0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
#Точність нашого послідовного класифікатора склала 71%.
