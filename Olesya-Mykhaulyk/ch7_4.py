# TODO
# ?????????
#

#Olesya Mykhaulyk
#ALs-12
# Chapter 7 Ex.4
import nltk
sentence=[('Mary','NN'),('saw','VBD'),('the','DT'),('cat','NN'),('sit','VB'),('on','IN'),('the','DT'),('mat','NN')]
grammar=r"""
      NP:{<DT|JJ|NN.*>+} // chunk sequences of DT,JJ,NN
      PP:{<IN><NP>} // chunk prepositions followed by NP
      VP:{<VB.*><NP|PP|CLAUSE>+$}// chunk verbs and their arguments
      CLAUSE:{<NP><VP>}//chunk NP, VP
"""

cp=nltk.RegexpParser(grammar) # testing created chunk parsel on the sentence
result = cp.parse(sentence) # print result
print result

#also we can display the result graphically by using the result.draw() option