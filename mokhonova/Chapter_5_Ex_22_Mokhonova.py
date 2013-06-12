# Chapter_5_Ex_22_Mokhonova
import nltk
import pprint
from nltk import RegexpTagger, word_tokenize
patterns = [
# створення сталих виразів
(r'(The|the|A|a|An|an)$', 'AT'), # артиклі
(r'(of|at|in|on|against)$', 'IN'), # прийменники
(r'.*ous$', 'JJ'), # прикметники
(r'.*ity$', 'NNJ'), # іменники, утворені від прикметників
(r'.*ly$', 'RB'), # прислівники
(r'.*self$|.*selves$', 'PRR'), # займенники

(r'.*ing$', 'VBG'), # герундій
(r'.*ed$', 'VBD'), # простий минулий
(r'.*es$', 'VBZ'), # 3 ос. одн. тепер. час
(r'.*ould$', 'MD'), # модальний
(r'.*\'s$', 'NN$'), # присвійні іменники
(r'.*s$', 'NNS'), # множина іменників
(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # кількісні числівники
(r'.*', 'NN'), # іменники за замовчуванням
]
regexp_tagger = RegexpTagger(patterns)
sentence = raw_input("Enter test sentence:\n")
pprint.pprint(regexp_tagger.tag(word_tokenize(sentence)))


