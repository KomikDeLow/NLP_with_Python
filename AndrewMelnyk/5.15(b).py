# TODO 
# unexpected indent
#

# Andrew Melnyk ALs-12

import nltk
from nltk.corpus import brown
sents=brown.tagged_sents(categories='news')
    def form_dict(sents):
    cfd = nltk.ConditionalFreqDist()
    for (wd, tg) in sents:
        cfd[wd].inc(tg)
    amb_dict = nltk.defaultdict()
    for w in cfd.conditions():
	    if len(cfd[w])>1:
		    amb_dict[w] = len(cfd[w])
    sortedDict = sorted(amb_dict.items(), reverse=True)
    return sortedDict

form_dict(nltk.corpus.brown.tagged_words(categories = 'news'))[:10]
[('you', 2), ('yield', 2), ('yet', 2), ('years', 2), ('year', 2), ('writing', 2), ('would', 2), ('worth', 2), ('worry', 2), ('works', 3)]

