# Fuyarchuk O. Chapter 6 Task 3
import nltk
import types
from nltk.corpus import senseval # ���������� �� ����� � �������
instances=senseval.instances('interest.pos')
features=[]# ������������ instances �� ��������� �������
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
    
size=int(len(features)*0.1)# ������������ ����� ����� ��� ����������
train_set, test_set=features[size:],features[:size]# ����� �� ��� �� �� ������� -
                                                    # ��� ���������� � ��� ����������
classifier=nltk.NaiveBayesClassifier.train(train_set)# ������� ������������
print nltk.classify.accuracy(classifier,test_set)# �������� ������� ���� ������
