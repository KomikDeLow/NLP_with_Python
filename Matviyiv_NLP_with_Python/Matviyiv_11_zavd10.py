#Building a simple search algorithm from the example from the book
#if this algorithm works, what should be the idea with the Indexes?
#The task undertakes building a list of all words with additional features, like the numbers of the act,line and so on?
import nltk
from nltk.etree.ElementTree import ElementTree

merchant_file = nltk.data.find('corpora/shakespeare/merchant.xml')
merchant = ElementTree().parse(merchant_file)


def Shakspire_search(word):
    list_of_index=[]
    for i, act in enumerate(merchant.findall('ACT')):
        for j, scene in enumerate(act.findall('SCENE')):
            for k, speech in enumerate(scene.findall('SPEECH')):
                for line in speech.findall('LINE'):
                    if word in str(line.text):
                        list_of_index.append([i+1,j+1,k+1,word])
    return list_of_index
list_result=Shakspire_search('music')
for i in range(10):
    print list_result[i]
