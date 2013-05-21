#Building a program which saves bouth feature sets and determines if
#they subsume each other
import nltk
fs1 = nltk.FeatStruct(BNUM=74, STREET='rue Pascal') # Building bouth feature sets
fs2= nltk.FeatStruct(BNUM=74, STREET= 'rue Pascal', CITY='Paris')

def subsumes_save_two_fs(fs1,fs2): # Building a function which saves both FS in a dictionary and determines which one subsumes which
    two_fs={}
    small_list1=[]
    for i in range(len(fs1)):
        small_list1.append((fs1.keys()[i], fs1[fs1.keys()[i]])) # making a list of features from fs1
    two_fs['fs1']=[small_list1]
    small_list2=[]
    for j in range(len(fs2)):
        small_list2.append((fs2.keys()[j], fs2[fs2.keys()[j]])) # making a list of features from fs2
    two_fs['fs2']=[small_list2]
    print 'FS1 subsumes FS2: ', fs1.subsumes(fs2)# cheking the subsumption
    print 'FS2 subsumes FS1: ', fs2.subsumes(fs1)
    return two_fs

result_dict={}
result_dict=subsumes_save_two_fs(fs1,fs2) # executing the function 
for j in range(len(result_dict)): # Printing out the fs1 and fs2 with their features
    print result_dict.items()[j-1]
