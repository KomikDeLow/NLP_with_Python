# TODO
# Comments ?
# What  different  pronunciations  and  parts-of-speech  are involved?
#

import nltk
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind.")
nltk.pos_tag(text)
print nltk.pos_tag(text)
