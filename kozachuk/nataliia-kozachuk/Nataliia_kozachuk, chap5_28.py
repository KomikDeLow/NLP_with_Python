#chapter 5, zadacha 28, Kozachuk Nataliia
 import nltk
st = nltk.corpus.treebank.tagged_words(simplify_tags=True)
# vukorustovyemo simplified fart-of-speech tagset
word_tag_fd = nltk.FreqDist(st)
#CHASTOTNA klasuficacia
noun=[word+"/" + tag for (word, tag) in word_tag_fd if tag.startswith ('N')]
#peregljadaemo najbilsh common nouns v teksti i sortyemo po ihnij chastoti
 print noun[:20]
 # vid 0 do 19
      word_tag_fd = nltk.FreqDist(nst)
us_noun=[word+"/" + tag for (word,tag) in word_tag_fd if tag.startswith('N')]
print us_noun [:20]
