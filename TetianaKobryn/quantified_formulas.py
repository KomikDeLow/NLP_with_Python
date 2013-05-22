# Presented by Tetiana Kobryn
#
# Chapter 10, Ex.3
# Translate sentences into quantified formulas of first-order logic.


import nltk
#a. Angus likes someone and someone likes Julia.
"""
exists a.(Angus(a) & s.(sb(s) & j.(Julia(j) -> like(a, s) & like(s, j)))
"""

print "a"
dom = set(['a', 'j', 's'])
v = """
     Angus => a
     Julia => j
     sb => s
     like => {(a, s), (s, j)}
     """
val = nltk.parse_valuation(v)
g = nltk.Assignment(dom, [('x', 'a'), ('y', 'j'), ('z', 's')])
m = nltk.Model(dom, val)
print m.evaluate('like(Angus, z) & like(sb, y)', g)


#b. Angus loves a dog who loves him.
"""
exists a.(Angus(a) & d.(dog(d) -> love(a, d) & love(d, a)))
"""

#c. Nobody smiles at Pat.
"""
¬∀x.(sb(x) & p.(Pat(p) -> smile(x,p)))
"""

#d. Somebody coughs and sneezes.
"""
exists x.(sb(x)->cough(x) & sneeze(x))
"""

#e. Nobody coughed or sneezed.
"""
¬∀x.(sb(x) -> cough(x) | sneeze(x))
"""

#f. Bruce loves somebody other than Bruce.
"""
exists b.(Bruce(b) & s.(sb(s) -> love(b, s) & ¬love(b, b)))
"""

#g. Nobody other than Matthew loves Pat.
"""
exists s.(sb(s) & m.(Matthew(m) & p.(Pat(p) -> love(m, p) & ¬love(s, p))))
"""

#h. Cyril likes everyone except for Irene.
"""
exists c.(Cyril(c) & all x.(everyone(x) & i.(Irene(i) -> like(c, x) & ¬like(c, i))))
"""

#i. Exactly one person is asleep.
"""
exists x(person(x) -> asleep(x))
"""
