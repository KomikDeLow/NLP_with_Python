import nltk
# declare the domain to the sentence a. Angus likes someone and someone likes Julia
dom1 = set(['b', 'o', 'c'])
v = """
Angus => b
someone => o
Julia => c
boy => {o}
girl => {b, c}
like => {(b, o), (o, c)}
"""
# convert a sequence of strings of the form symbol => value into a Valuation object using the utility function parse_valuation()
val = nltk.parse_valuation(v)
# display the result
print val

# declare the domain to the sentence b. Angus loves a dog who loves him.
dom2 = set(['b', 'o'])
v = """
angus => b
dog => o
boy => {b}
love => {(b, o), (o, b)}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence c. Nobody smiles at Pat.
dom3 = set(['b', 'o'])
v = """
nobody => b
pat => o
boy => {o}
smile => {(b, o)}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence d. Somebody coughs and sneezes.
dom4 = set(['b'])
v = """
somebody => b
cough => {b}
sneeze => {b}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence e. Nobody coughed or sneezed.
dom5 = set(['b'])
v = """
nobody => b
cough => {b}
sneeze => {b}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence f. Bruce loves somebody other than Bruce.
dom6 = set(['b', 'o'])
v = """
bruce => b
somebody => o
boy => {b}
love => {(b, o)}
other => {(o, b)}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence g. Nobody other than Matthew loves Pat.
dom7 = set(['b', 'o', 'c'])
v = """
nobody => b
matthew => o
pat => c
love => {(b, c), (o, c)}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence h. Cyril likes everyone except for Irene.
dom8 = set(['b', 'o', 'c'])
v = """
cyril => b
everyone => o
Irene => c
like => {(b, o)}
except => {(b, c)}
"""
val = nltk.parse_valuation(v)
print val

# declare the domain to the sentence i. Exactly one person is asleep.
dom9 = set(['b'])
v = """
person => b
exactly one => {b}
asleep => {b}
"""
val = nltk.parse_valuation(v)
print val

