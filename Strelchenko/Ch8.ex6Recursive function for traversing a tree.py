import nltk
t = nltk.Tree (' (S (NP Ann) (VP cought (NP flu)))')
def traverse (t):
    try:                   # building a recursive funtion
        t.node
    except  AttributeError :
        print t,
    else:
        print '(', t.node,
        for child in t:
               traverse(child) # traversing a treebank 
        print ')',
print t.height()  # output
nltk.Tree.draw (t)

