# by Ivanna Kushniruk
import nltk
hz = set (['a','s', 'f','j'])
p = """
     Angus => a
     Julia => j
     sb1 => s 
     sb2 => f  
     like => {(a, s), (f, j)}
     """
val = nltk.parse_valuation(p)
t = nltk.Assignment(hz, [('x', 'a'), ('y', 'j'), ('z', 's'), ('u', 'f')])
m = nltk.Model(hz, val)
print 'Angus likes someone and someone likes Julia: exists x. exists z. exists u. exist y. (like(x, z) & like(u, y)'
print m.evaluate('exists x. exists z. exists y. exist u (like(x, z) & like(u, y))', t)

zh = set (['a', 'd'])
d = """
    Angus => a
    dog => d
    love => {(a,d), (d,a)}
    """
val = nltk.parse_valuation (d)
k = nltk.Assignment(zh, [('x', 'a'), ('y','d')])
m = nltk.Model(zh, val)
print 'Angus loves a dog who loves him: exist x. exist y. (love(x,y)&love(y,x))'
print m.evaluate ('exist x. exist y. (love(x,y)&love(y,x))', k)

bz = set (['n', 'p'])
d = """
    Nobody => n
    Pat => p
    smile => {-(n,p)}
    """
val = nltk.parse_valuation (d)
k = nltk.Assignment(bz, [('x', 'n'), ('y','p')])
m = nltk.Model(bz, val)
print 'Nobody smiles at Pat: exists x. exists y. -(smile(x,y))'
print m.evaluate ('exists x. exists y. -(smile(x,y))', k)

print 'Somebody coughs and sneezes: exists x.(coughs(x) & sneezes(x))'
print 'Nobody coughed or sneezed: all x. -(coughed(x) | sneezed(x))'
print 'Bruce loves somebody other than Bruce: exists b. exists s. (-(love(b, b) & love(b, s)))'
print 'Nobody other than Matthew loves Pat: exists s. exists m. exists p. (-(love(s, p) & love(m, p)))'
print 'Cyril likes everyone except for Irene:exists c. all s. exists i. (-like(c, i) & like(c, s)))'
print 'Exactly one person is asleep: exists x. (asleep(x))'







