# Chubko Uliana Al-12
import nltk
fs_main=nltk.FeatStruct(A='X',B='X')# основний набір функцій
fs1=nltk.FeatStruct(A='X')
fs2=nltk.FeatStruct(B='X')# subsumed structures
print 'fs1 subsumes fs_main: ',fs1.subsumes(fs_main)
print 'fs2 subsumes fs_main: '# дивимося,чи побудована нами структура підноситься до основної нашої структури
