# Shylimova K. Al-13
# Chapter 7, task 9

import nltk
true_sentence = "I have been here for a long time"
true_sentence = nltk.sent_tokenize(true_sentence)
true_sentence = [nltk.word_tokenize(word) for word in true_sentence]
true_sentence = [nltk.pos_tag(word) for word in true_sentence]
grammar = r'''
   NP: {<DT|JJ|NN.*>+}
   PP{<IN><NP>}
   VP: {<VB.*><NP|PP|CLAUSE>+$}
   CLAUSE: {<NP><VP>}'''
wrong_sentence = [("I","PRO"),("have","VB"),("been","VN"),
                  ("here","ADV"),("for","P"),("a","DT"),
                  ("long","JJ"),("time","NN")]
parser = nltk.RegexpParser(grammar)
print true_sentence[0]
print wrong_sentence
print parser.parse(true_sentence[0])
print parser.parse(wrong_sentence)
