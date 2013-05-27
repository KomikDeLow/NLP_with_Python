# fine
# Bahen Diana, PRLs-11, Chapter 9, Exercise 9

import nltk
fs_main=nltk.FeatStruct("[A=?x,B=?x]")# main feature set
# subsumed structures
fs1=nltk.FeatStruct("[A=?x]")
fs2=nltk.FeatStruct("[B=?x]")
# cheking if subsumed structures are in main structure
print 'fs1 subsumes fs_main: ',fs1.subsumes(fs_main)
print 'fs2 subsumes fs_main: ', fs2.subsumes(fs_main)
