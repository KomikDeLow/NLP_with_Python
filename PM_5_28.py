import nltk
# experiment with taggers using the simplified tagset
nltk.corpus.brown.tagged_words()
[('The', 'AT'), ('Fulton', 'NP-TL'), ...]
nltk.corpus.brown.tagged_words(simplify_tags=True)
[('The', 'DET'), ('Fulton', 'NP'), ('County', 'N'), ...]
# Оскільки у першому випадку, ми маємо повний набір тегів, то бачимо, що такий тегсет дає детальнішу інформацію про слова ('Fulton', 'NP-TL'), тоді як спрощений—менше ('Fulton', 'NP'). Отже, доцільніше використовувати повний набір тегів для більш повної інформації щодо слів.
