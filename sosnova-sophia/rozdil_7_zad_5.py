import nltk
grammar = r"""
          NP: {<DT|NN>?<VGB><NN>}"""
# ������� �������
sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"), (",", ","), ("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
cp = nltk.RegexpParser(grammar)
# ������� ���������
print cp.parse(sentence)
#�������
sentence = [('This', 'DT'), ('tactic', 'JJ'), ('has', 'VBZ'), ('proven', 'VBN'), ('successful', 'JJ'), ('for', 'IN'), ('some', 'DT'), (',', ','), ('however', 'RB'), ('most', 'RBS'), ('people', 'NNS'),('do', 'VBP'), ('not', 'RB'), ('enjoy', 'VB'), ('utilizing', 'VGB'), ('this', 'DT'), ('technique', 'NN'), ('or', 'CC'), ('being', 'VBG'), ('on', 'IN'), ('the', 'DT'), ('receiving', 'VBG'), ('end', 'NN'), ('of', 'IN'), ('the', 'DT'), ('tactic', 'JJ'), ('.', '.')]
# ������� ��� ��������
cp = nltk.RegexpParser(grammar)
#������� ���������
print cp.parse(sentence)
#������� ���������
