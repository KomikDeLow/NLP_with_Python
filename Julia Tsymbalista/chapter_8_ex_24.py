#Iuliia Tsymbalista ALs-13
#chapter 8, task 24
#task:
#Write a recursive function that produces a nested bracketing for a tree, leaving
#out the leaf nodes and displaying the non-terminal labels after their subtrees. So
#the example in Section 8.6 about Pierre Vinken would produce: [[[NNP NNP]NP ,
#[ADJP [CD NNS]NP JJ]ADJP ,]NP-SBJ MD [VB [DT NN]NP [IN [DT JJ NN]NP]PP-CLR
#[NNP CD]NP-TMP]VP .]S. Consecutive categories should be separated by space.

# for this task I use a parsed sentence from file wsj_0017.mrg;

import nltk
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0017.mrg')[0]
print 'Sentence'
print t # printing our sentence
answer_list=[]
answer_list.insert(0,t.node)


# a recursive function:

def rec_tree(tree1): 
    small_list=[]
    if not tree1.height()>3: # Checkig the heigth of the tree
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


# Printing out recursive tree and drawing the parsed sentence
print 'recursive tree'
print answer_list
t.draw() 
