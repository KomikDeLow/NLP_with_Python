import nltk
# experiment with taggers using the simplified tagset
nltk.corpus.brown.tagged_words()
[('The', 'AT'), ('Fulton', 'NP-TL'), ...]
nltk.corpus.brown.tagged_words(simplify_tags=True)
[('The', 'DET'), ('Fulton', 'NP'), ('County', 'N'), ...]
# ������� � ������� �������, �� ���� ������ ���� ����, �� ������, �� ����� ������ �� ��������� ���������� ��� ����� ('Fulton', 'NP-TL'), ��� �� �������������� ('Fulton', 'NP'). ����, ��������� ��������������� ������ ���� ���� ��� ���� ����� ���������� ���� ���.
