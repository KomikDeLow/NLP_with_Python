# Fuyarchuk O. Chapter 6 Task 3
import nltk
import types
from nltk.corpus import senseval # доступаємся до даних з корпусів
instances=senseval.instances('interest.pos')
features=[]# перетворюємо instances до потрібного вигляду
for inst in instances:
    w=[]

	
for i in inst.context:
    if type(i)==types.TupleType:
	    w.append(i)
    elif type(i)==types.StringType:
	    w.append(("None",i))
    a={"word":inst.word,"position":inst.position,}
    b=dict(w)
    a.update(b)
    features.append((a,' '.join(inst.senses)))
    
size=int(len(features)*0.1)# встановлюємо розмір даних для тестування
train_set, test_set=features[size:],features[:size]# ділимо всі дані на дві частини -
                                                    # для тренування і для тестування
classifier=nltk.NaiveBayesClassifier.train(train_set)# тренуємо класифікатор
print nltk.classify.accuracy(classifier,test_set)# оцінюємо точність його роботи
