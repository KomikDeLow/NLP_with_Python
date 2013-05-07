# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#розділ 8 завдання 26
#Modify the functions init_wfst() and complete wfst() so that the contents of
#each cell in the WFST is a set of non-terminal symbols rather than a single
#non-terminal
#Встановлюємо просту граматику
#заповнення таблиці wfst відбувається коли вводиться ф-кція init,початкові
#нетермінальні символи,які відповідають значенню речення
#import nltk
#groucho_grammar = nltk.parse_cfg("""
#S -> NP VP
# PP -> P NP
#NP -> Det N | Det N PP | 'I'
#VP -> V NP | VP PP
#Det -> 'an' | 'my'
#N -> 'elephant' | 'pajamas'
#V -> 'shot'
#P -> 'in'
#""")
#в результаті її роботи отримуємо повністю заповнену матрицю,в якій є
#нетермінальні символи
#def init_wfst(tokens, grammar):
   # numtokens = len(tokens)
   # wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
   # for i in range(numtokens):
       # productions = grammar.productions(rhs=tokens[i])
       # wfst[i][i+1] = productions[0].lhs()
    #return wfst
      # робимо морфологічний аналіз,розширирюємо інформацію комірки матриці,
      # аналізуємо як працюють ці функції.Для цього використовуємо ф-кцію tokens
#tokens = "I shot an elephant in my pajamas".split()
#wfst0 = init_wfst(tokens, groucho_grammar)
#def display(wfst, tokens):
    #print '\nWFST ' + ' '.join([("%-4d" % i) for i in range(1, len(wfst))])
    #for i in range(len(wfst)-1):
      #  print "%d   " % i,
       # for j in range(1, len(wfst)):
           # print "%-4s" % (wfst[i][j] or '.'),
       # print
#display(wfst0, tokens)
#numtokens список слів речення
#range(7+1) ряд складається з 7 слів
#wfst = [[None for i in range(7+1)] for j in range(7+1)] формується матриця,
       #i,j змінюється в межах від 1 до 7
#wfst
#groucho_grammar.productions(rhs=tokens[0])в результаті ми змінній product
      # присвоюємо значення правила контекстно-вільної граматики,де права
      # частина відовідає tokens зі значенням 0
#[NP -> 'I']
#groucho_grammar.productions(rhs=tokens[1]) слова з індексом 1 є правою частиною
      # правила
#[V -> 'shot']
#groucho_grammar.productions(rhs=tokens[2])
#groucho_grammar.productions(rhs=tokens[0])[0].lhs()
       #акцептор використовує добре сформовану підрядкову таблицю
#def init_wfst(tokens, grammar):
  #  numtokens = len(tokens) список слів речення
   # wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
   # for i in range(numtokens): цикл відбувається стільки разів,скільки є
   #елементів
       # productions = grammar.productions(rhs=tokens[i])
       # wfst[i][i+1] = str((productions[0].rhs(),productions[0].lhs())) значен-
      # ня лівої частини правила
      # змінюємо координати центру діагоналі матриці,в комірці записуватимуться
       #значення лівої частини граматики
    #return wfst

#wfst0 = init_wfst(tokens, groucho_grammar)
#display(wfst0, tokens)
#def init_wfst(tokens, grammar):
   # numtokens = len(tokens) список слів речення
# wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
   # for i in range(numtokens): цикл відбувається стільки разів,скільки є
  # елементів
   #записуємо праву комірку в ліву,отримуємо модернізовану функцію
        #productions = grammar.productions(rhs=tokens[i])
  # 
       # wfst[i][i+1] = productions[0].lhs()
   # return wfst
   #цикл використовуватиметься лише 1 раз
#def complete_wfst(wfst, tokens, grammar, trace=False): приймає вже заповнену
   #таблицю,речення,граматику
   # index = dict((p.rhs(), p.lhs()) for p in grammar.productions()) формує
   #словник і в нього записуються правила контекстно-вільної граматики.Ключем
   #є права частина,а ліва всіх правил граматики
   
   # numtokens = len(tokens)
    #for span in range(2, numtokens+1): мінімальне значення приймає значення
   #від 2 до 7
       # for start in range(numtokens+1-span): цикл відбувається стільки разів,
       #скільки є елементів
           # end = start + span
           # for mid in range(start+1, end): 
               # nt1, nt2 = wfst[start][mid], wfst[mid][end] значення матриці,
              # що заповнюється
               # #if nt1 and nt2 and (nt1,nt2) in index: перевіряємо чи є така
               #права частина у нашій граматиці
                   # wfst[start][end] = index[(nt1,nt2)] записуємо ліву частину
                  # граматики
                  #  if trace:
                      #  print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                       # (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
    #return wfst
#range(2, 7+1)
#range(7+1-2)
#range(0+1, 2)
#wfst0[0][1]
#wfst[1][2]
#wfst0[1][2]
#def complete_wfst(wfst, tokens, grammar, trace=False):
   # index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
   # numtokens = len(tokens)
    #for span in range(2, numtokens+1):
       # for start in range(numtokens+1-span):
            #end = start + span
            #for mid in range(start+1, end):
                #nt1, nt2 = wfst[start][mid], wfst[mid][end]
                #if nt1 and nt2 and (nt1,nt2) in index:
                  #  wfst[start][end] = str(((nt1,nt2),index[(nt1,nt2)])) запи-
                 # сує не тільки ліву частину,а й праву
                   # if trace:
                      #  print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                        #(start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
    #return wfst

#wfst0[0][1][0]
#wfst0[0][1].split()
#wfst0[0][1].split()[1]
#wfst0[0][1].split()[1][:-1]
#def complete_wfst(wfst, tokens, grammar, trace=False):
   # index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    #numtokens = len(tokens)
    #for span in range(2, numtokens+1):
       # for start in range(numtokens+1-span):
           # end = start + span
           # for mid in range(start+1, end):
              #  nt1, nt2 = wfst[start][mid].split()[1][:-1], wfst[mid][end].split()[1][:-1]
               # if nt1 and nt2 and (nt1,nt2) in index:
                  #  wfst[start][end] = str(((nt1,nt2),index[(nt1,nt2)]))
                  #  if trace:
                      #  print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                       # (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
   # return wfst
#def complete_wfst(wfst, tokens, grammar, trace=False):
   # index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    #numtokens = len(tokens)
   # for span in range(2, numtokens+1):
       # for start in range(numtokens+1-span):
          #  end = start + span
            #for mid in range(start+1, end):
               # nt1, nt2 = wfst[start][mid], wfst[mid][end]
               # if nt1 and nt2 and (nt1,nt2) in index:
                   # wfst[start][end] = str(((nt1,nt2),index[(nt1,nt2)]))
                   # if trace:
                       # print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                       # (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
   # return wfst
#wfst1 = complete_wfst(wfst0, tokens, groucho_grammar)
#display(wfst1, tokens)
#wfst0 = init_wfst(tokens, groucho_grammar)
#wfst1 = complete_wfst(wfst0, tokens, groucho_grammar)
#display(wfst1, tokens)
