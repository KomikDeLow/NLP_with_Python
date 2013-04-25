#Presented by Tetiana Kobryn

#Chapter 8, Ex.20
#To compare multiple trees in a single window, we can use the draw_trees()
#method. Define some trees and try it out.


from nltk.corpus import treebank
from nltk.draw.tree import draw_trees
# defining trees using  Penn Treebank Corpus
tree1 = treebank.parsed_sents('wsj_0001.mrg')[0]
tree2 = treebank.parsed_sents('wsj_0002.mrg')[0]
tree3 = treebank.parsed_sents('wsj_0003.mrg')[4]
#presenting these trees, drawing them
draw_trees(tree1, tree2, tree3)
