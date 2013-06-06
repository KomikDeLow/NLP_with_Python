# Chapter_7_Ex_4_Mokhonova
import nltk
sentence=[('Mary','NN'),('saw','VBD'),('the','DT'),('cat','NN'),('sit','VB'),('on','IN'),('the','DT'),('mat','NN')]
grammar=r"""
      NP:{<DT|JJ|NN.*>+} // chunk sequences of DT,JJ,NN
      PP:{<IN><NP>} // chunk prepositions followed by NP
      VP:{<VB.*><NP|PP|CLAUSE>+$}// chunk verbs and their arguments
      CLAUSE:{<NP><VP>}//chunk NP, VP
"""

cp=nltk.RegexpParser(grammar) # testuju chunk parsel v rechenni
result = cp.parse(sentence) # vuvodzhu resul'tat
print result

