# Lesia Martsyniuk, ALs-12
import nltk
main_fs=nltk.FeatStruct(A='X',B='X')# Main Feture set

fsA=nltk.FeatStruct(A='X')# subsume struxtures
fsB=nltk.FeatStruct(B='X')

print 'fsA subsumes main_fs: ',fs1.subsumes(main_fs)# cheking if the builded Structures subsume the main structure
print 'fsB subsumes main_fs: ', fs2.subsumes(main_fs)
