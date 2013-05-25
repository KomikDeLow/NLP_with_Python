# Shylimova K. Al-13
# Chapter 8, task 23

import nltk
sentence = """What was more, the in his turn somewhat 
    youngish Nikolay Parfenovich also turned
    out to be the only person in the entire world 
    to acquire a sincere liking to our 'dis-criminated-against' 
    public procurator."""
sentence = nltk.sent_tokenize(sentence)
sentence = [nltk.word_tokenize(word) for word in sentence]
sentence = [nltk.pos_tag(word) for word in sentence]
print sentence
