# Khrystyna Maschakevich, AL-13, exercise 22
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
my_text_to_regex = ['One', 'night', 'at', 'the', 'dinner', 'table', 'the', 'wife', 'commented', ',', '“',
                        'When', 'we', 'were', 'first', 'married', ',', 'you', 'took', 'the', 'small', 'piece',
                        'of', 'steak', 'and', 'gave', 'me', 'the', 'larger', '.', 'Now', 'you', 'take', 'the',
                        'large', 'one', 'and', 'leave', 'me', 'the', 'smaller', ';', 'You', 'don’t', 'love',
                        'me', 'any', 'more', '…”', '“', 'Nonsense', ',', 'darling', ',', '”', 'replied', 'the',
                        'husband', ',', '“', 'you', 'just', 'cook', 'better', 'now', '.', '”']
regexp_tagger = nltk.RegexpTagger(miracle_regex)
a=regexp_tagger.tag(brown_sents[3])
b=regexp_tagger.tag(my_text_to_regex)
 
