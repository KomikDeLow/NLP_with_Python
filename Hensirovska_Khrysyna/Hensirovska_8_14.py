# TODO
# I need Python modul.
#

#����������� ��������,����-12
#����� 8,�������� 14
#You can modify the grammar in the recursive descent parser demo by selecting
#Edit Grammar in the Edit menu. Change the first expansion production, namely
#NP -> Det N PP, to NP -> NP PP. Using the Step button, try to build a parse tree.
#What happens?
#import nltk
#sent = ['I', 'loved', 'rain'] ��������� �������
#������������ ������ ����������-����� ��������� ��� ���������� �������
#grammar1 = nltk.parse_cfg("""
#S -> NP VP
#NP -> DET N PP
#NP -> "I"
#VP -> V NP
#V -> "loved"
#NP -> "rain"
#""")
#sent = "I loved rain".split()
#�������� ������������� ������
#rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3)
#�������� ���������� �� �����
#result = rd_parser.parse(sent)
#�������� ������� ���������� �� �����
#result.draw()
#����� � ������ ������ ������ ������� �� ���������.�������� NP -> Det N PP,
#�� NP -> NP PP
#grammar1 = nltk.parse_cfg("""
#S -> NP VP
#NP -> NP PP
#NP -> "I"
#VP -> V NP
#V -> "loved"
#NP -> "rain"
#""")
#sent = "I loved rain".split()
#�������� ������������� ������
#rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3)
#�������� ���������� �� �����
#result = rd_parser.parse(sent)
#ϳ��� ��������� ������� �� ��������� ���������� ����������.
