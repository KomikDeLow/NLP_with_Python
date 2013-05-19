#Presented by Iuliia Tsymbalista
#Chapter 7, ex.2


#Write a tag pattern to match noun phrases containing plural head nouns, e.g.,
#many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS. Try
#to do this by generalizing the tag pattern that handled singular noun phrases




# wablon tegiv dlia vraxuvannia imennykiv v mnozhyni
import nltk
from nltk import *
tagged_tokens = [("many ", "JJ"), ("researchers","NNS"),("two", "CD"),("weeks", "NNS"), ("new","JJ"),("positions","NNS"),("big","JJ"),("dog","NN")]
cp = nltk.RegexpParser("NP: {<DT|CD|PP\$|JJ.*|>?<JJ.*>?<NNS>+}")
print cp.parse(tagged_tokens)

#wablon tegiv dlia vraxuvannia imennykiv v odnuni
tagged_tokens_singular = [("many ", "JJ"), ("researchers","NNS"),("two", "CD"),("weeks", "NNS"), ("new","JJ"),("positions","NNS"),("big","JJ"),("dog","NN")]
cp = nltk.RegexpParser("NP: {<DT|CD|PP\$|JJ.*|>?<JJ.*>?<NN>+}")
print cp.parse(tagged_tokens_singular)

#wablon tegiv dlia vraxuvannia imennykiv v odnuni ta mozhyni
tagged_tokens_singular_plural = [("many ", "JJ"), ("researchers","NNS"),("two", "CD"),("weeks", "NNS"), ("new","JJ"),("positions","NNS"),("big","JJ"),("dog","NN")]
cp = nltk.RegexpParser("NP: {<DT|CD|PP\$|JJ.*|VBG>?<JJ.*>?<NN.*>+}")
print cp.parse(tagged_tokens_singular_plural)
