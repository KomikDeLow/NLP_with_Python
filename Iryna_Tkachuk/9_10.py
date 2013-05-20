#Presented by Tkachuk Iryna
#
#9_10.Ignoring structure sharing, give an informal algorithm for unifying two
#feature structures.



import nltk
#define some features
fs1 = nltk.FeatStruct("[SPOUSE = [ADDRESS = [CITY = Paris]]]")
fs2 = nltk.FeatStruct("""[NAME=Lee, ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'],
                            SPOUSE=[NAME=Kim, ADDRESS->(1)]]""")
print fs1.unify(fs2)#unifying 2 features
