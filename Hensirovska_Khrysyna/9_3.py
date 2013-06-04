#Khrystyna Hensirovska,ALs-12
#Chapter 9,task 3
#Write a function subsumes() that holds of two feature structures fs1 and fs2 just
#in case fs1 subsumes fs2.
import nltk
#�� ������������� �-���� FeatStruct  ��� ���������� ��������� �������� � NLTK
#ֳ ���������� ������ �������� ��������  string ��� integer.�������� ���������
#� ����� ����� ��������,����,�� ����������� �� ���� �������� �������
#�������������.�� ������ ��������������� ��� ��������� ���������,��� ���������
#�������� ��� ������������.
fs1=nltk.FeatStruct("[C =?x,A = [B = ?x]]")
#��������� ���������� ���������,��� �� ������� ��������
fs2=nltk.FeatStruct("[D =?x,C =?x,A = [B = ?x]]")
print fs1.subsumes (fs2) #��������� �� fs1 �������� � fs2
print fs2.subsumes (fs1)#��������� �� fs2 �������� � fs1
#�� ��������� �����-���� �� ��"������ �� ������� ��������� fs1 �� fs2,� ����
#�������,���� fs1 �������� � fs2
def subs (fs1, fs2):
	if fs1.subsumes (fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes (fs1):
		print fs2.unify(fs1)
	else: print "None"
	print subs(fs1,fs2)
