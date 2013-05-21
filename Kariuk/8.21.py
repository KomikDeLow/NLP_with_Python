# Rostyslav Kariuk PRLs-11
# Rozdil_8, Zadacha_21

from nltk corpus import treebank
first_sents=treebank.parsed_sents()[:99]
for i in first_sents:
	print i[0][:2]