 import nltk
 from nltk.corpus import brown
 d={'iphone':'apple''nexus4''Google-LG'}
 #����� ��� ��������
 d['htc desire x']='HTC'
 # ���������� �������� ��������� ����
 print d['xyz']

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print d['xyz']
KeyError: 'xyz'
 #��� ������ �������
