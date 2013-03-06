from __future__ import division
import nltk
from nltk.corpus import brown
tagged_words=brown.tagged_words()
tagged_words_conditional_freq=nltk.ConditionalFreqDist((word,tag)for(word,tag)
                                                       in tagged_words)
tagged_words_with_only_one_tag=[word for word in
                                tagged_words_conditional_freq.conditions()
                                if len(tagged_words_conditional_freq[word])==1]

vidnoshennya=(len(tagged_words_with_only_one_tag)*100)/len(tagged_words)
print 'The proportion of words that will always be assigned to the same part-of-speech is = ', vidnoshennya

tagged_words_with_more_than_one_tag=[word for word
                                     in tagged_words_conditional_freq.conditions()
                                     if len(tagged_words_conditional_freq[word])>=2]
print 'There are ', len(tagged_words_with_more_than_one_tag), ' words that have more than one tag.'
vidnoshennya2=(len(tagged_words_with_more_than_one_tag)*100)/len(tagged_words)
print 'The persentage of ambiguous words is = ', vidnoshennya2, ' %'
