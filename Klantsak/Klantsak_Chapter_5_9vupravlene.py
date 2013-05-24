# TODO
# Модуль не містить коментарів

# Veronika KLantsal ALs-11
#
import nltk
from nltk.corpus import brown
text1 = nltk.word_tokenize("Go away!")#zrobula tokenizaciyu perwogo rechennya
nltk.pos_tag(text1)# python vuznachae wo "Go" e imennukom y rechenni "Go away"
# Ce nepravul'ne vuznachennya oskil'ku "Go" e dieslovo
text2 = nltk.word_tokenize("We went on the excursion.")#tokenizaciya drygogo rechennya
nltk.pos_tag(text2)# rezyl'tat: "went" dieslovo y munylomy chasi
print  nltk.pos_tag(text1)
print  nltk.pos_tag(text2)
