
# Проблема з "None" тегами у тому, що як сказано в документації:
# In articular, for each context ``c`` in the training data,
# set ``_context_to_tag[c]`` to the most frequent tag for that context.
# Отже, буде протегована інакше ніж в цьому ж реченні на тренуванні,
# якщо б вона частіше попадалась в іншому контексті. Проте, при недостатньому
# розмірі даних для навчання, наступна біграма не зможе бути протегована, оскільки
# це слово ще не попадалось поряд із таким тегом. В результаті решті слів у реченні
# буде присвоєно тег "None".

import pprint
import nltk
from nltk.corpus import brown
SCALE = 0.003
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * SCALE)
train_sents = brown_tagged_sents[:size]
test_sents = brown_sents[:size]
bigram_tagger = nltk.BigramTagger(train_sents, verbose=True)
count = 0
for index, sent in enumerate(test_sents):
    for tag in bigram_tagger.tag(sent):
        if tag[1] is None:
            print "Incorrectly tagged sentence:"
            pprint.pprint(bigram_tagger.tag(sent))
            print "Manually tagged, was on training:"
            pprint.pprint(train_sents[index])
            count += 1
            break

print "Sentences with 'None' / Size of train corpus:\n{}/{}".format(count, size)        
            

            
