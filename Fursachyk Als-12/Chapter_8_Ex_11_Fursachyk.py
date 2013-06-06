#Chapter_8_Ex_11_Fursachyk
import nltk
from nltk import Tree
help(Tree) #strichka dokumentaciji funkciji Tree
sentence= ['He','wants','drink'] #stvorjuemo rechennya
#opysuemo prostu gramatyku dlya rechennya
grammar1 = nltk.parse_cfg("""  
   	#S -> NP VP 
   	#NP -> "He" 
   	#VP -> V NP 
   	#V -> "wants" 
   	#NP -> "drink" 
   	# """)

sentence= "He wants drink".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3) #programa syntaksychnogo analizu
       	#vyvodymo syntaksychnyj analiz
for tree in rd_parser.nbest_parse(sentence):
   print tree
 #vyvodymo grafichne zobrazhennya dereva
result.draw()

