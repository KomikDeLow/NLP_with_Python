#���������� �, ����-11, ������ �3, �����5
# TODO
# Comments ?
# What  different  pronunciations  and  parts-of-speech  are involved?
#
# "�������� ������� ����� ��� ������� ����" what is it mean?
# "���� �������� ���� ������� ����� � ������" ??
# Bad style (modul name, string (line) lenght)

import nltk
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind.")
nltk.pos_tag(text)
print nltk.pos_tag(text)
# POS tagger ��������� ����������� ��� � �������� ������� ����� ��� ������� ����. ���������� �������� ��������, �� ����� 'They' - ���������, 'wind'-䳺�����, 'back'-���������, 'the'-�������, 'clock'-��������, 'while'-���������, 'we'-���������, 'chase'-䳺�����, 'after'-���������, 'the'-�������, 'wind'- �������.   
#����� POS tagger ������� ���� �������� ���� ������� ����� � ������. ��������� ����� wind ���������� 2 ����, ������ ��� ���� ������� 䳺������, � ������-���������.
