# NameError: name 'fs1' is not defined

#Building two structures which subsume the main one
#the main structure consists of two features, with the same values "?x"

import nltk
main_fs=nltk.FeatStruct(A='X',B='X')# Main Feture set

fsA=nltk.FeatStruct(A='X')# subsume struxtures
fsB=nltk.FeatStruct(B='X')

print 'fsA subsumes main_fs: ',fs1.subsumes(main_fs)# cheking if the builded Structures subsume the main structure
print 'fsB subsumes main_fs: ', fs2.subsumes(main_fs)
