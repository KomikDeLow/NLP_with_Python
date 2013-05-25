
# Dyrda Roksolana, AL-13 
import nltk
#Use the simplified tagset to the tagged Brown Corpus
with_simplified_tagset = nltk.corpus.brown.tagged_words(categories='news', simplify_tags=True) 
#Define which of these tags are the most common in the 'news' category of the Brown Corpus
word_tag_fd = nltk.FreqDist(with_simplified_tagset) 
#Sort the nouns which have the tag with the first letter 'n' by frequency
noun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')] 
#Print the list of these nouns with tags
print 'With simplified tagset %s\n'%noun[:20] 
#The simplified tagset is not used
without_simplified_tagset = nltk.corpus.brown.tagged_words(categories='news', simplify_tags=False) 
#Once more define the most common tags  in the 'news' category of the Brown Corpus
word_tag_fd = nltk.FreqDist(without_simplified_tagset) 
#Once more sort the nouns which have the tag with the first letter 't' by frequency
noun1=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')] 
#Once more print the list of nouns with tags
print 'Without simplified tagset %s\n'% noun1[:20] 
#The first list of nouns (with simplified tagset) contains except nouns also numerals. 
#The second list of nouns (without simplified tagset) contains only nouns. 

 
