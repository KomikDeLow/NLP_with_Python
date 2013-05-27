# fine

#Building a program which times work of tree parsers
#a top-to-down parser, down-to-top parser and a leftcorner parser
#
import timeit
import nltk
from nltk.corpus import *
#Building a grammar for the tree simple sentences
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> DT NP | JJ NN
VP -> BEZ VP | VBD IN
DT -> "This" | "His"
JJ -> "new" | "old" | "beautiful"
NN -> "car" | "elephant" | "dog"
BEZ -> "is"
VBD -> "parked" | "fed" | "caught"
IN -> "outside" | "inside"
""")
# Copiying the grammar above to a different module to have a possibility ti import it
sent1='This new car is parked outside'.split()
sent2='This old elephant is fed outside'.split() # Used sentenses
sent3='His beautiful dog is caught inside'.split()

timer_top_Sent1=timeit.timeit("""
import nltk
from grammar import grammar1
sent1='This new car is parked outside'.split()
top_down_parser = nltk.RecursiveDescentParser(grammar1)
par1=top_down_parser.parse(sent1)
""", number=100) # Timing a top to down parser sentence 1

timer_top_Sent2=timeit.timeit("""
import nltk
from grammar import grammar1
sent2='This old elephant is fed outside'.split()
top_down_parser = nltk.RecursiveDescentParser(grammar1)
par1=top_down_parser.parse(sent2)
""", number=100)

timer_top_Sent3=timeit.timeit("""
import nltk
from grammar import grammar1
sent3='His beautiful dog is caught inside'.split()
top_down_parser = nltk.RecursiveDescentParser(grammar1)
par1=top_down_parser.parse(sent3)
""", number=100)


timer_down_Sent1=timeit.timeit("""
import nltk
from grammar import grammar1
sent1='This new car is parked outside'.split()
down_top_parse = nltk.ShiftReduceParser(grammar1)
par2=down_top_parse.parse(sent1)
""", number=100) # Timing a down to top parser sentense1

timer_down_Sent2=timeit.timeit("""
import nltk
from grammar import grammar1
sent2='This old elephant is fed outside'.split()
down_top_parse = nltk.ShiftReduceParser(grammar1)
par2=down_top_parse.parse(sent2)
""", number=100)

timer_down_Sent3=timeit.timeit("""
import nltk
from grammar import grammar1
sent3='His beautiful dog is caught inside'.split()
down_top_parse = nltk.ShiftReduceParser(grammar1)
par2=down_top_parse.parse(sent3)
""", number=100)

# Building a Left-Corner Parser
# Copying all functions to another module to have a possibility of importing them and timing
def init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        wfst[i][i+1] = productions[0].lhs()
    return wfst

def complete_wfst(wfst, tokens, grammar, trace=False):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    numtokens = len(tokens)
    for span in range(2, numtokens+1):
        for start in range(numtokens+1-span):
            end = start + span
            for mid in range(start+1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end]
                if nt1 and nt2 and (nt1,nt2) in index:
                    wfst[start][end] = index[(nt1,nt2)]
                    if trace:
                        print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                        (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
    return wfst

def display(wfst, tokens):
    print '\nWFST ' + ' '.join([("%-4d" % i) for i in range(1, len(wfst))])
    for i in range(len(wfst)-1):
        print "%d " % i,
        for j in range(1, len(wfst)):
            print "%-4s" % (wfst[i][j] or '.'),
        print



timer_corner_Sent1=timeit.timeit("""
import nltk
from grammar import grammar1
from grammar import init_wfst
from grammar import complete_wfst
from grammar import display
sent1='This new car is parked outside'.split()
wfst0 = init_wfst(sent1, grammar1)
wfst1 = complete_wfst(wfst0, sent1, grammar1)
""", number=100) # Timing a Left Corner parser on sentense 1

timer_corner_Sent2=timeit.timeit("""
import nltk
from grammar import grammar1
from grammar import init_wfst
from grammar import complete_wfst
from grammar import display
sent2='This old elephant is fed outside'.split()
wfst0 = init_wfst(sent2, grammar1)
wfst1 = complete_wfst(wfst0, sent2, grammar1)
""", number=100)

timer_corner_Sent3=timeit.timeit("""
import nltk
from grammar import grammar1
from grammar import init_wfst
from grammar import complete_wfst
from grammar import display
sent3='His beautiful dog is caught inside'.split()
wfst0 = init_wfst(sent3, grammar1)
wfst1 = complete_wfst(wfst0, sent3, grammar1)
""", number=100)

print 'Table Representing time taken by parsers to parse a simple sentences:' # Building a table to present all time data
print '                 Sent1','           Sent2','           Sent3'
print 'Top_Down parser ',timer_top_Sent1,' ',timer_top_Sent2,' ',timer_top_Sent3
print 'Down_Top parser ',timer_down_Sent1,' ',timer_down_Sent2,' ',timer_down_Sent3
print 'Left_Cor parser ',timer_corner_Sent1,' ',timer_corner_Sent2,' ',timer_corner_Sent3

#To time the results i had to build another module and store my grammar in it
#so it could be imported and be timed (i am providing the module of the grammar to)
