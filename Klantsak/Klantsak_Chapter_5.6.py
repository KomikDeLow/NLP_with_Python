# Veronika Klantsak ALs-11

# Try deleting an element from a dictionary d, using the syntax del d['abc'].
# Check that the item was deleted.

d = {} # create an empty dictionary
d['cat']='NN'
d['little']='JJ'
d['walk']='V'
d['gladly']='ADV' # filling the dictionary
print d
# {'walk': 'V', 'cat': 'NN', 'gladly': 'ADV', 'little': 'JJ'}
del d['little'] # delete an element of dictionary
print d
# {'cat': 'NN', 'walk': 'V', 'gladly': 'ADV'}
