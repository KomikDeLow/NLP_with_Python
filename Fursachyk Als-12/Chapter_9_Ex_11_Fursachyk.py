#Chapter_9_Ex_11_Fursachyk
import nltk
from nltk import load_parser
tokens = 'Heute sieht der Hund die Katze'.split() # речення, в якому дієслово знаходиться на другому місці перед підметом
                                                
cp = load_parser('grammars/book_grammars/german_modified.fcfg') # змінена граматика, до якої я додала 2 рядки
                                                                # Adverbs
                                                                #ADV -> 'Heute'
# роблю граматичний розбір речення зі зміненою німецькою граматикою
for tree in cp.nbest_parse(tokens):
    print tree

tree.draw()
