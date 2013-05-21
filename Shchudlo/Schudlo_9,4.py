
#Adding a BAR - subcategory feature to determine Parent -> child 
# relation ships in the grammar

Grammar(30) page 345

VP[TENSE=?t, NUM=?n] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n]
VP[TENSE=?t, NUM=?n] -> V[SUBCAT=trans, TENSE=?t, NUM=?n] NP
VP[TENSE=?t, NUM=?n] -> V[SUBCAT=clause, TENSE=?t, NUM=?n] SBar

V[SUBCAT=intrans, TENSE=pres, NUM=sg] -> 'disappears' | 'walks'
V[SUBCAT=trans, TENSE=pres, NUM=sg] -> 'sees' | 'likes'
V[SUBCAT=clause, TENSE=pres, NUM=sg] -> 'says' | 'claims'

V[SUBCAT=intrans, TENSE=pres, NUM=pl] -> 'disappear' | 'walk'
V[SUBCAT=trans, TENSE=pres, NUM=pl] -> 'see' | 'like'
V[SUBCAT=clause, TENSE=pres, NUM=pl] -> 'say' | 'claim'

V[SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked'
V[SUBCAT=trans, TENSE=past] -> 'saw' | 'liked'
V[SUBCAT=clause, TENSE=past] -> 'said' | 'claimed'

#Adding the BAR feature

V[TENSE=?t, NUM=?n, BAR=1] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n, BAR=0]
V[TENSE=?t, NUM=?n, BAR=1] -> V[SUBCAT=trans, TENSE=?t, NUM=?n, BAR=0] NP # I do not specify the BAR[feature] for NP
V[TENSE=?t, NUM=?n, BAR=1] -> V[SUBCAT=clause, TENSE=?t, NUM=?n, BAR=0] SBar # and SBar as the gramar doesn't specify how many leves they can have

V[SUBCAT=intrans, TENSE=pres, NUM=sg, BAR=0] -> 'disappears' | 'walks'
V[SUBCAT=trans, TENSE=pres, NUM=sg, BAR=0] -> 'sees' | 'likes'
V[SUBCAT=clause, TENSE=pres, NUM=sg, BAR=0] -> 'says' | 'claims'

V[SUBCAT=intrans, TENSE=pres, NUM=pl, BAR=0] -> 'disappear' | 'walk'
V[SUBCAT=trans, TENSE=pres, NUM=pl, BAR=0] -> 'see' | 'like'
V[SUBCAT=clause, TENSE=pres, NUM=pl, BAR=0] -> 'say' | 'claim'

V[SUBCAT=intrans, TENSE=past, BAR=0] -> 'disappeared' | 'walked'
V[SUBCAT=trans, TENSE=past, BAR=0] -> 'saw' | 'liked'
V[SUBCAT=clause, TENSE=past, BAR=0] -> 'said' | 'claimed'
