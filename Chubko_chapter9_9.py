# Chubko Uliana Al-12
import nltk
fs_main=nltk.FeatStruct(A='X',B='X')# �������� ���� �������
fs1=nltk.FeatStruct(A='X')
fs2=nltk.FeatStruct(B='X')# subsumed structures
print 'fs1 subsumes fs_main: ',fs1.subsumes(fs_main)
print 'fs2 subsumes fs_main: '# ��������,�� ���������� ���� ��������� ���������� �� ������� ���� ���������
