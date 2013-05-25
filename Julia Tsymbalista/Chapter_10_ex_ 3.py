#Iuliia Tsymbalista ALs-13
# capter 10, ex.3

# the following sentences are translated into quantified formulas of first-order logic.
# the utility function parse_valuation() is used for  converting a sequence of strings of
# the form symbol => value into a Valuation object.

import nltk

#a. Angus likes someone and someone likes Julia.
# exists x. exists y. exists z. (like(x, y) & like(y, z))

dom = set(['x', 'y', 'z'])
v = """
     Angus => x
     Julia => z
     someone  => y
     like  => {(x, y), (y, z)}
     """
val2 = nltk.parse_valuation(v)
print 'example a'
print val2


# b. Angus loves a dog who loves him.
# exists x. exists y. (love(x, y) & love(y, x))

dom = set(['x', 'y'])
v = """
     Angus => x
     dog => y
     love  => {(x, y), (y, x)}
     """
val2 = nltk.parse_valuation(v)
print 'example b'
print val2


# c. Nobody smiles at Pat.
# all x.(person(x) -> exists y.(person(y) & doesn't_smile(x,y)))


dom = set(['x', 'y'])
v = """
     Nobody => x
     Pat => y
     doesn't_smile => {(x, y)}
     """
val2 = nltk.parse_valuation(v)
print 'example c'
print val2



# d. Somebody coughs and sneezes.
# exists x.(coughs(x) & sneezes(x))
dom = set(['x'])
v = """
     Somebody => x
     coughs => {(x, x)}
     sneezes => {(x, x)}
     """
val2 = nltk.parse_valuation(v)
print 'example d'
print val2

# e. Nobody coughed or sneezed.
# the same as previous
# all x.(person(x) -> -(coughed(x) | sneezed(x))


#f. Bruce loves somebody other than Bruce.
# exists x. exists y. (-(love(x, x) & love(x, y)))

dom = set(['x', 'y'])
v = """
     Bruce => x
     somebody => y
     love => { -(x, x),(x, y)}
     """
val2 = nltk.parse_valuation(v)
print 'example f'
print val2

#g. Nobody other than Matthew loves Pat.
# exists x. exists y. exists z. (-(love(x, z) & love(y, z)))


#h. Cyril likes everyone except for Irene.
# exist x. exists y. exists z. (-like(y, z) & like(y, x)))

dom = set(['x', 'y', 'z'])
v = """
     Cyril => y
     everyone => x
     Irene => z
     like => {-(y, z)(y, x), }
     """
val2 = nltk.parse_valuation(v)
print 'example h'
print val2


#i. Exactly one person is asleep.
#(asleep(x))


dom = set(['x'])
v = """
     person => x
     asleep => {(x)}
     """
val2 = nltk.parse_valuation(v)
print 'example i'
print val2
