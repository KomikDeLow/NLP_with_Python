# Chapter_7_Ex_4_Fursachyk
import nltk
sentence=[('Mary','NN'),('saw','VBD'),('the','DT'),('cat','NN'),('sit','VB'),('on','IN'),('the','DT'),('mat','NN')]
grammar=r"""
      NP:{<DT|JJ|NN.*>+} // chunk sequences of DT,JJ,NN
      PP:{<IN><NP>} // chunk prepositions followed by NP
      VP:{<VB.*><NP|PP|CLAUSE>+$}// chunk verbs and their arguments
      CLAUSE:{<NP><VP>}//chunk NP, VP
"""

cp=nltk.RegexpParser(grammar) # testujemo stvorenyj chunk parsel v rechenni
result = cp.parse(sentence) # vuvodymo resul'tat
print result

