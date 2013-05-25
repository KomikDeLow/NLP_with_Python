#iryna Ros, PRLs-11, chapter 9, exercise 5
#Modify the German grammar.
nltk.data.show_cfg('grammars/book_grammars/german.fcfg')
% start S
# Grammar Productions
S -> NP[CASE=nom, AGR=?a] VP[AGR=?a]
NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a]
NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
VP[AGR=?a] -> V[AGR=?a]
VP[AGR=?a] -> V[OBJCASE=?c, AGR=?a] NP[CASE=?c]
# Lexical Productions
# Singular determiners
# masc
Det[CASE=nom, AGR=[GND=masc,PER=3,NUM=sg]] -> 'der'
Det[CASE=dat, AGR=[GND=masc,PER=3,NUM=sg]] -> 'dem'
Det[CASE=acc, AGR=[GND=masc,PER=3,NUM=sg]] -> 'den'
# fem
Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
# neu
Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'das'
Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'dem'
Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'das'
# Plural determiners
Det[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'die'
Det[CASE=dat, AGR=[PER=3,NUM=pl]] -> 'den'
Det[CASE=acc, AGR=[PER=3,NUM=pl]] -> 'die'
# Nouns
N[AGR=[GND=masc,PER=3,NUM=sg]] -> 'Tisch'
N[CASE=nom, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Tische'
N[CASE=dat, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Tischen'
N[CASE=acc, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Tische'
N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Frau'
N[AGR=[GND=fem,PER=3,NUM=pl]] -> 'Frauen'
# Pronouns
PRO[CASE=nom, AGR=[PER=1,NUM=sg]] -> 'ich'
PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'mich'
PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'mir'
PRO[CASE=nom, AGR=[PER=2,NUM=sg]] -> 'du'
PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'dich'
PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'dir'
PRO[CASE=nom, AGR=[PER=3,NUM=sg]] -> 'er' | 'sie' | 'es'
PRO[CASE=nom, AGR=[PER=1,NUM=pl]] -> 'wir'
PRO[CASE=acc, AGR=[PER=1,NUM=pl]] -> 'uns'
PRO[CASE=dat, AGR=[PER=1,NUM=pl]] -> 'uns'
PRO[CASE=nom, AGR=[PER=2,NUM=pl]] -> 'ihr'
PRO[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'sie'
# Verbs
V[AGR=[SUBCAT=intrans ,NUM=sg,PER=1]] -> 'gehe'
V[AGR=[ SUBCAT=intrans ,NUM=sg,PER=2]] -> 'gehest'
V[AGR=[ SUBCAT=intrans ,NUM=sg,PER=3]] -> 'geht'
V[AGR=[ SUBCAT=intrans ,NUM=pl, PER=1]] -> 'gehen'
V[AGR=[ SUBCAT=intrans ,NUM=pl, PER=2]] -> 'geht'
V[AGR=[ SUBCAT=intrans ,NUM=pl, PER=3]] -> 'gehen'
V[OBJCASE=acc, AGR=[ SUBCAT=trans ,NUM=sg,PER=1]] -> 'mache' | 'mag'
V[OBJCASE=acc, AGR=[ SUBCAT=trans, NUM=sg,PER=2]] -> 'machst' | 'magst'
V[OBJCASE=acc, AGR=[ SUBCAT=trans, NUM=sg,PER=3]] -> 'macht' | 'mag'
V[OBJCASE=dat, AGR=[ SUBCAT=trans, NUM=sg,PER=1]] -> 'Schlafe' | 'helfe'
V[OBJCASE=dat, AGR=[ SUBCAT=trans, NUM=sg,PER=2]] -> 'Schlafst' | 'hilfst'
V[OBJCASE=dat, AGR=[ SUBCAT=trans, NUM=sg,PER=3]] -> 'Schlaft' | 'hilft'
V[OBJCASE=acc, AGR=[ SUBCAT=trans, NUM=pl,PER=1]] -> 'machen' | 'moegen'
V[OBJCASE=acc, AGR=[ SUBCAT=trans, NUM=pl,PER=2]] -> 'macht' | 'moegt'
V[OBJCASE=acc, AGR=[ SUBCAT=trans, NUM=pl,PER=3]] -> 'machen' | 'moegen'
V[OBJCASE=dat, AGR=[ SUBCAT=trans, NUM=pl,PER=1]] -> 'Schlafen' | 'helfen'
V[OBJCASE=dat, AGR=[ SUBCAT=trans, NUM=pl,PER=2]] -> 'Schlaft' | 'helft'
V[OBJCASE=dat, AGR=[ SUBCAT=trans, NUM=pl,PER=3]] -> 'Schlafen' | 'helfen'
