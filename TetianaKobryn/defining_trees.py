# fine
#Presented by Tetiana Kobryn

#Chapter 8, Ex. 5
#a. Write code to produce two trees, one for each reading of the phrase old men
#and women.
#b. Encode any of the trees presented in this chapter as a labeled bracketing,
#and use nltk.Tree() to check that it is well-formed. Now use draw() to display
#the tree.
#c. As in (a), draw a tree for The woman saw a man last Thursday.

import nltk
from nltk.draw.tree import draw_trees

"""
a.
"""
# Create Trees
t1 = nltk.Tree('NP', ['men', 'and', 'women'])
tree_a1 = nltk.Tree('ADJP', ['old', t1])
print "First reading of the phrase old men and women"
print tree_a1

t2 = nltk.Tree('NP', ['old', 'men'])
tree_a2 = nltk.Tree('NP', [t2, 'and', 'women'])
print "Second reading of the phrase old men and women"
print tree_a2

"""
b.
"""
t_1 = nltk.Tree('NP', ['the', 'little', 'yellow', 'dog'])
t_2 = nltk.Tree('NP', ['the', 'cat'])
t_3 = nltk.Tree('PP', ['at', t_2])
t_4 = nltk.Tree('VP', ['barked', t_3])
tree_b = nltk.Tree('S', [t_1, t_4])
print tree_b
tree_b.draw()

"""
c.
"""
#Sentence: The dog saw a man in the park
#Defining trees
tc1 = nltk.Tree('NP', ['The', ' dog'])
tc2 = nltk.Tree('NP', ['the', 'park'])
tc3 = nltk.Tree('PP', ['in', tc2])
tc4 = nltk.Tree('NP', ['a','man', tc3])
tc5 = nltk.Tree('VP', ['saw', tc4])
tree_c1 = nltk.Tree('S', [tc1, tc5])

tc_1 = nltk.Tree('NP', ['The', ' dog'])
tc_2 = nltk.Tree('NP', ['the', 'park'])
tc_3 = nltk.Tree('PP', ['in', tc_2])
tc_4 = nltk.Tree('NP', ['a','man'])
tc_5 = nltk.Tree('VP', ['saw', tc_4, tc_3])
tree_c2 = nltk.Tree('S', [tc1, tc_5])
#presenting these trees, drawing them
draw_trees(tree_c1, tree_c2) 


