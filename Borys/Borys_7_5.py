# Roman Borys PRLs-11
import nltk
#Setting grammar rule
grammar = r"""
NP:{<DT|NN>?<VBG><NN>}"""
#NP:{<DT|NN>?<VBG><NN>}"""
sentence = [("the","DT"),("receiving","VBG"),("end","NN"),(",",","),
           ("assistant","NN"),("managing","VBG"),("editor","NN")]
#Creating parser
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)
sentence= [("A","DT"),("dark","JJ"),("red","JJ"),("car","NN"),
          ("came","VBD"),("to","IN"),("a","DT"),("stopt","NN"),("in","IN"),
           ("front","NN"),("of","IN"),("the","DT"),("Flynn-Fletcher","JJ"),
           ("residence","NN"),("that","WDT"),("same","JJ"),("evening","NN"),
           (",",","),("in","IN"),("another","DT"),("demension","NN"),(".",".")]
#Creating chunk parser
cp= nltk.RegexpParser(grammar)
print cp.parse(sentence)
