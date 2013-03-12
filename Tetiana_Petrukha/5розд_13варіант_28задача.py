import nltk
st = nltk.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(st)
noun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')]
print noun[:20]
print('')
nst = nltk.corpus.treebank.tagged_words(simplify_tags=False)
word_tag_fd = nltk.FreqDist(nst)
us_noun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')]
print us_noun [:20]
