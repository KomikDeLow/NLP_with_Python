#nataliia Kozachuk 9_1

import nltk
grammar1 = nltk.parse_cfg("""
S -> NP_SG VP_1st_SG
S -> NP_SG VP_3rd_SG
NP_SG -> Pro
VP_1st_SG -> Cop_1st_SG_Adj
VP_3rd_SG -> Cop_3rd_SG_Adj
Cop_1st_SG ->'am'
Cop_3rd_SG ->'is'
PRO -> 'I' | 'She'
Adj -> 'happy'
Cop -> 'is | am '
""")
print grammar1
# we want to avoid the original grammar being multiplied ( I is happy, They am happy)
