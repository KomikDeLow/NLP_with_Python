#Finding tree vebs in the PP atachment corpus
#and Building a table where you can see noun1 used with verb "make"
#and how many times it is used in differnet attachments but with the same noun1
import nltk
from nltk.corpus import *
entries = nltk.corpus.ppattach.attachments('training') # Buiklding a list of all entries
verbs1=['do','play','make'] # Building a list of verbs
verb_entries=[w for w in entries if w.verb in verbs1] # taking out entries that have given verbs
print 'Entries with vebs "do","play","make" :',len(verb_entries)

verb_make=[w for w in entries if w.verb=='make'] # A list of entries with only verb "make"

confd=nltk.ConditionalFreqDist((word.noun1,word.attachment) for word in verb_make) # Building a conditional FreqDist to show the frequense of noun1 usege with diferent attachments
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print 'Table representing all noun1 words used with verb "make" and how many times they are used in different attachments:'
print confd.tabulate() # Building a table to show the results

word_list=[]
for word in verb_make:
    word_list.append(word.noun1) # list of all noun1 used with "make"

list_test=[]
for w in word_list:
    if len(confd[w].items())>1:
        list_test.append(('noun1: '+w,confd[w].items()[0],confd[w].items()[1])) # Building a list of noun1 entries that are used with bouth attachments

fd=nltk.FreqDist(list_test) # building a list with no dublings
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print 'Table representing noun1 used with verb "make" and in bouth attechments, + how many times :'
for w in fd.keys():
    print w # displaying the list


# Hope this partially correct, but I don't know how to do the "b" part of this task
