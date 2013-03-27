#presented by Iryna Tkachuk PRLc-13
#Search the Web for spoof newspaper headlines,
#find gems as:British Left Waffles on Falkland Islands,
#and Juvenile Court to Try Shooting Defendant.
#tag these headlines to see whether knowledge of the part-of-speech
#tags removes the ambiguity.

import nltk
from nltk.corpus import brown

def tag_text(text):
    """ Tokenizes text and tags each word. """
    tokens = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    return tagged_words

if __name__ == '__main__':
    phrases = ["British Left Waffles on Falkland Islands.",
               "Juvenile Court to Try Shooting Defendant."]
    print 'Manual tagging of popular phrases:'
    for ph in phrases:
        print "Phrase: %s, Tagged words: %s" % (ph, tag_text(ph))
