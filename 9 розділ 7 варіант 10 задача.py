>>> import nltk
>>> fs0=nltk.FeatStruct(CITY='Los Angeles',STREET='Washington',RESTAURANT='New life')
>>> fs1=nltk.FeatStruct(MENU='China',DECOR='Modern')
>>> print fs1.unify(fs0)
[ CITY       = 'Los Angeles' ]
[ DECOR      = 'Modern'      ]
[ MENU       = 'China'       ]
[ RESTAURANT = 'New life'    ]
[ STREET     = 'Washington'  ]
>>>
