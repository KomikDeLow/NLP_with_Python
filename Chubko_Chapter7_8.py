# TODO
# It isn't Python modul
#
#

Python 2.6.6 (r266:84297, Aug 24 2010, 18:46:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 2.6.6      
>>> import nltk
>>> grammar=""" #створила граматику
NP:
{<DT>?<JJ>*<NN><NNS>*}#створила послідовність чанк для DT JJ NN NNS
}<VBP|IN>+{           # створила чанк послідовність для VBP IN
cp=nltk.RegexpParser (grammar)# створила синтаксичний аналізатор для речення з прикладу
sentence=[('Small','JJ'),('beautiful','JJ'),('cats','NNS'),('stay','VBP',),('on','IN'),('the','DT'),('yard','NN'),('and','CC'),('look','VBP'),('on','IN'),('the','DT'),('blue','JJ'),('sky','NN')# синтаксичний аналізатор для мого речення
print cp.parse(sentence)#результат
from nltk.corpus import con112000# імпортували корпус 112000 для оцінки
cp=nltk.Regexp.Parser(grammar)# створила синтаксичний аналізатор для речення прикладу
test_sents=nltk.corpus.con112000.chunked_sents('test.txt', chunk_types=('NP',))
print 'Accuracy=',nltk.chunk.accuracy(cp,test_sents)#видрукували оцінку
