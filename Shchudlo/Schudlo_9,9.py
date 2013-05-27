# fine

#Building two feature structures which would subsume the main Feture structure
#which consists of two features "A" and "B", and which have the same values "?x"
import nltk
fs_main=nltk.FeatStruct(A='X',B='X')# Buiding a main Feture set

fs1=nltk.FeatStruct(A='X')# Building subsume struxtures
fs2=nltk.FeatStruct(B='X')

print 'fs1 subsumes fs_main: ',fs1.subsumes(fs_main)# cheking if the builded Structures subsume the main structure
print 'fs2 subsumes fs_main: ', fs2.subsumes(fs_main)
