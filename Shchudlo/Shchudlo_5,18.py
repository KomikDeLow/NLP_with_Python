# fine
#TODO
# Comments?
# If there are  8729  words that have more than one tag 
# and the persentage of ambiguous words is =  0.751727535154  %
# then there are only 11612?

# Creating a program to determine how many words have only one tag, and how many have more than one.
from __future__ import division
import nltk
from nltk.corpus import brown
tagged_words=brown.tagged_words() # making a list of all words
list_dot=['.',',','/','!','?','"','..','...',':','-','(',')',';']
tagged_words222=[]
for w in tagged_words: # cleaning all words by deleting punctuations
    if w[0] not in list_dot:
        tagged_words222.append(w)



tagged_words_conditional_freq=nltk.ConditionalFreqDist((word,tag)for(word,tag)
                                                       in tagged_words222) # building a conditional FreqDist
tagged_words_with_only_one_tag=[word for word in
                                tagged_words_conditional_freq.conditions()
                                if len(tagged_words_conditional_freq[word])==1] # creating a list of words with only one tag

vidnoshennya=(len(tagged_words_with_only_one_tag)*100)/len(set(tagged_words222)) # evaluating the percentage of words with only one tag
print 'The proportion of words that will always be assigned to the same part-of-speech is = ', vidnoshennya, '%'

tagged_words_with_more_than_one_tag=[word for word
                                     in tagged_words_conditional_freq.conditions()
                                     if len(tagged_words_conditional_freq[word])>=2] # creating a list of words that have more than one tag
print 'There are ', len(tagged_words_with_more_than_one_tag), ' words that have more than one tag.'
vidnoshennya2=(len(tagged_words_with_more_than_one_tag)*100)/len(set(tagged_words222)) # evaluating the percentage
print 'The persentage of ambiguous words is = ', vidnoshennya2, ' %'
