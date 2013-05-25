# Roman Borys PRLs-11

from nltk.corpus import treebank
from nltk.draw.tree import draw_trees
# using Penn Treebank Corpus
tree1 = treebank.parsed_sents('wsj_0001.mrg')[0]
tree2 = treebank.parsed_sents('wsj_0002.mrg')[0]
tree3 = treebank.parsed_sents('wsj_0003.mrg')[4]
#Drawing trees
draw_trees(tree1, tree2, tree3)