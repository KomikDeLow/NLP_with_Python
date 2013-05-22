# Chubko Uliana Al-12
import nltk
from nltk import *
sentence=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('NP',))[99]
grammar=r"NP:{<[CDJNP].*>+}
# опис граматики,що виділятиме регулярні вирази, що описуватимуть послідвні вирази
# (CD J NP)
cp=nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print sentence
print result
result.draw()
