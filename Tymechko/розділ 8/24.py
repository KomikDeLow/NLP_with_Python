# Building a recursive program which leaves the leaves of the tree and
# wrigths down the structure of the sentense in a recursive way
import nltk
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0] # Getting out the sentence we will work with on
answer_list=[]
answer_list.insert(0,t.node)# Wrigthing the 'S' symbole

def rec_tree(tree1): # Building a recursive function
    small_list=[]
    if not tree1.height()>3: # Checking the length of the tree
        if tree1.height()<3:
            small_list.insert(0,tree1.node) # Inserting into sub-list
        else:
            small_list2=[]
            small_list.insert(0,tree1.node)
            for i in tree1:
                small_list2.insert(0,i.node) 
            small_list.insert(0,small_list2)
    else:
        small_list3=[]
        small_list.insert(0,tree1.node)
        for i in tree1:
            small_list3.insert(0,rec_tree(i))
        small_list.insert(0,small_list3)
    return small_list

# Wrigting down trees in backwards order
for tree in t: 
	answer_list.insert(0,rec_tree(tree))
# Printing out recursive tree
print answer_list 
t.draw() # Drawing the normal parsed sentense to compare
