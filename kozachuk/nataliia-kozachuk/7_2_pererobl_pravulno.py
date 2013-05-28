##Ch 7.2.
# Write a tag pattern to match noun phrases containing plural head nouns, e.g.,
#many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS. Try
#to do this by generalizing the tag pattern that handled singular noun phrases.
import nltk
from nltk.corpus import brown
pattern='NP: {<DT>?<JJ.*>?<CD>?<NNS>}'##bydyemo tag pattern
sent=[('Many','JJ'), ('researchers','NNS'), ('two','CD'), ('weeks','NNS'), ('both','DT'), ('new','JJ'), ('positions','NNS')]
##our sentence
cp=nltk.RegexpParser(pattern)
print cp.parse(sent)
