# Fuyarchuk O. Chapter 8 task 8b
import nltk
t1=nltk.Tree('(S(NP I)(VP(VP(V shot) (NP(Det an) (N elefant))) (PP((P in) (NP((Det my) (N pajamas)))))))')
t1.draw()
t2=nltk.Tree('(S((NP((Det the)(Nom((Adj little)(N bear)))))(VP((VP(V saw)(NP(Det the)(Nom(Adj fine)(Adj fat)(N trout))))(PP(P in)(NP(Det the)(Nom(N brook))))))))')
t2.draw()
t3=nltk.Tree('(S((NP(Det the)(Nom((Adj angry)(Nom(N bear)))))(VP(V chased)(NP((Det the)(Nom((Adj little)(N squirrell))))))))')
t3.draw()
t4=nltk.Tree('(S((NP(PropN Chattere))(VP(V said)(S(NP(PropN Buster))(VP(V thought)(S((NP((Det the)(N tree)))(VP(V was)(Adj tall)))))))))')
t4.draw()

