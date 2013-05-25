# Veronika KLantsak ALs-11

#% start S
# ###################
# Grammar Productions
# ###################
# S expansion productions
# S -> NP[NUM=?n] VP[NUM=?n]
# S -> NP[NUM=?n,COUNT=?C] VP[NUM=?n]
# NP expansion productions
# NP[NUM=?n] -> N[NUM=?n]
# NP[NUM=?n,COUNT=?C] -> Det[COUNT=?C] N[NUM=?n]
# NP[NUM=pl] -> N[NUM=pl]
# VP expansion productions
# VP[TENSE=?t, NUM=?n] -> V[TENSE=?t, NUM=?n]
# VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj
# ###################
# Lexical Productions
# ###################
# Det[COUNT=def] -> 'the' 
# N[NUM=sg] -> 'boy' | 'water' 
# N[NUM=pl] -> 'boys' 
# V[TENSE=pres, NUM=sg] -> 'sing' 
# V[TENSE=pres, NUM=pl] -> 'sings'
# Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
# Adj -> 'precious'



# V anglijskij movi e vuznachenui artukl' “the”, wo slygye dlya vuznachennya abo
# identufikacii imennuka, i nevuznachenui artukl' “a” (“an” pered golosnumu), 
# wo vkazye na nevuznachenui imennuk. 

# Y nastypnux prukladax mozhemo bachutu, wo y perwux trjox vupadkax 
# konkretuzaciyu (ytochnennya), a inwi dva prukladu e gramatuchno nepravul'ni, 
# oskil'ku povunen bytu artukl' vuznachosti “à”.

# Tretij vupadok - pered nezlichennumu imennukamu, wo oznachayut' rechovuny, 
# masy, yakwo ne vkazyet'sya kil'kist' ciei rechovunu artukl' ne vzhuvaet'sya.


# a. The boy sings.
# b. *Boy sings.

# a. The boys sing.
# b. Boys sing.

# a. The water is precious.
# b. Water is precious.
