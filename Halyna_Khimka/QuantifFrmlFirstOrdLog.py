# Halyna Khimka
# Quantified Formulas of first-order logic
# Chapter 10.3

import nltk

#a. Angus likes someone and someone likes Julia.
# exists a. exists b. exists c. exists d.(like(a,b)&like(c,d))

"""
I have chosen for someone two form symbols and two valuations.
Angus likes someone but it doesn't mean that the same someone likes Julia.
But if I have chosen the same valuea for both someones, it would mean that Angus likes the same someone and this someone likes Julia.
"""
dom=set(['a', 'b', 'c', 'd'])
v="""
    Angus => a
    someone1 => b
    someone2 => c
    Julia => d
    like =>{(a, b),(c, d)}
"""
val=nltk.parse_valuation(v)
print 'Angus likes someone and someone likes Julia.'
print val

# b) Angus loves a dog who loves him.
# exists a. exists b (love(a,b)and love(b,a))

dom=set(['a', 'b'])
v="""
   Angus => a
   dog => b
   love => {(a,b),(b,a)}
"""
val1 = nltk.parse_valuation(v)
print 'Angus loves a dog who loves him'
print val1

# c) Nobody smiles at Pat.
# all a. exists b.(smile(a,b))
dom=set(['a','b'])
v="""
   Nobody => a
   Pat => b
   smile =>{a,b}
   """
val2=nltk.parse_valuation(v)
print 'Nobody smiles at Pat.'
print val2

# d) Somebody coughs and sneezes.
# exists a.(cough(a) & sneeze(a))
dom=set(['a'])
v="""
   Somebody => a
   cough => {(a)}
   sneeze => {(a)}
   """
val3=nltk.parse_valuation(v)
print 'Somebody coughs and sneezes.'
print val3

# e) Nobody coughed or sneezed.
# exists a.(cough(a) & sneeze(a))
dom=set(['a'])
v="""
   Nobody => a
   cough => {(a)}
   sneeze => {(a)}
   """
val4=nltk.parse_valuation(v)
print 'Nobody coughs and sneezes.'
print val3

# d) Bruce loves somebody other than Bruce.
print 'Bruce loves somebody other than Bruce.'
print 'exists a. exists b. (love(a,b)&-(a,a))'
dom=set['a', 'b']
v="""
   Bruce=>a
   somebody=>b
   love => {(a,b),-(a,a)}
   """
print nltk.parse_valuation(v)


