#Irena Marunyshyn PRLs-12 Chapter7 Ex 5
#Write a tag pattern to cover noun phrases that contain gerunds, e.g., the/DT
#receiving/VBG end/NN, assistant/NN managing/VBG editor/NN. Add these patterns
#to the grammar, one per line. Test your work using some tagged sentences of your
#own devising.
import nltk
grammar = r"""
NP:{<DT|NN>?<VBG><NN>}"""# create a chunk parser.chunk determiner(DT)/noun(NN),gerund(VBG) and noun(NN) 
sentence = [("the","DT"),("receiving","VBG"),("end","NN"),(",",","), ("assistant","NN"),("managing","VBG"),("editor","NN")]# test it on our example sentence
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)# result  is a tree
