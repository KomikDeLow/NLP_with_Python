import nltk
#a) Angus likes someone and someone likes Julia.
"""
exists a. exists c. exists b. (like(a, s) & like(s, b))
"""

dom1 = set(['a', 'b', 'c'])
v = """
Angus => a
Julia => b
someone => c
like => {(a, c), (c, b)}
"""
val = nltk.parse_valuation(v)
print "a)", val

#b) Angus loves a dog who loves him.
"""
exists b. exists d. (love(b, d) & love(d, b))
"""
dom2 = set(['b', 'o'])
v = """
angus => b
dog => d
boy => {b}
love => {(b, d), (d, b)}
"""
val = nltk.parse_valuation(v)
print "b)", val

#c) Nobody smiles at Pat.
"""
- exists n. exists p. (smile(n,p))
"""
dom3 = set(['n', 'p'])
v = """
Nobody => n
Pat => p
smile => {-(n, p)}
"""
val = nltk.parse_valuation(v)
print "c)", val


#d) Somebody coughs and sneezes.
"""
exists x.(coughs(x) & sneezes(x))
"""
dom4 = set(['b'])
v = """
somebody => b
cough => {(b, b)}
sneeze => {(b, b)}
"""
val = nltk.parse_valuation(v)
print "d)",val

#e) Nobody coughed or sneezed.
"""
all x.(person(x) -> -(coughed(x) | sneezed(x))
"""
dom5 = set(['b'])
v = """
nobody => b
cough => {(b, b)}
sneeze => {(b, b)}
"""
val = nltk.parse_valuation(v)
print "e)", val

#f) Bruce loves somebody other than Bruce.
"""
exists b. exists s. (-(love(b, b) & love(b, s)))
"""
dom6 = set(['b', 's'])
v = """
Bruce => b
sb => s
love => {(b, s), -(b, b)}
"""
val = nltk.parse_valuation(v)
print "f)", val

#g) Nobody other than Matthew loves Pat.
"""
exists n. exists m. exists p. (-(love(n, p) & love(m, p)))
"""
dom7 = set(['n', 'm', 'p'])
v = """
nobody => n
matthew => m
pat => p
love => {(n, p), (m, p)}
"""
val = nltk.parse_valuation(v)
print "g)",val

#h) Cyril likes everyone except for Irene.
"""
exists c. all e. exists i. (-like(c, i) & like(c, e)))
"""
dom8 = set(['c', 'e', 'i'])
v = """
Cyril => c
everyone => e
Irene => i
like => {(c, e), -(c, i)}
"""
val = nltk.parse_valuation(v)
print "h)", val

#i) Exactly one person is asleep.
"""
(asleep(p))
"""
dom9 = set(['p'])
v = """
person => p
asleep => {(p)}
"""
val = nltk.parse_valuation(v)
print "i)", val
