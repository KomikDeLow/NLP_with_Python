# Shylimova K. Al-13
# Chapter 9, task 3

import nltk
fs1 = nltk.FeatStruct(SIZE=42, COLOUR='Black')
fs2 = nltk.FeatStruct(NAME='T-shirt')
print fs1.subsumes(fs2)
print fs2.subsumes(fs1)
fs3 = nltk.FeatStruct(SIZE=42)
print fs3.subsumes(fs1)
fs4 = fs1.unify(fs2)
print fs4
def shop(fsx,fsy):
    if fsx.subsumes(fsy):
        print fsx.unify(fsy) 
    else:
       print 'fsx ne vxodut v fsy'
print shop(fs1,fs2)
print shop(fs3,fs1)
