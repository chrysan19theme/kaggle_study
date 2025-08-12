#7.1
years_list=[1998,1999,2000,2001,2002]

#7.2
print(years_list[3])

#7.3
print(years_list[-1])

#7.4
things=['mozzarella','cinderella','salmonella']

#7.5
things[1]=things[1].capitalize()
print(things)

#7.6
things[0]=things[0].upper()
print(things)

#7.7
del things[2]
print(things)

#7.8
surprise=['Groucho','Chico','Harpo']

#7.9
surprise[-1]=surprise[-1].lower()
print(surprise)
surprise.reverse()
print(surprise)
surprise[0]=surprise[0].capitalize()
print(surprise)

#7.10
even=[number for number in range(10) if number % 2==0]
print(even)

#7.11
start1=['fee','fie','foe']
rhymes=[
    ('flop','get a mop'),
    ('fope','turn the rope'),
    ('fa','get your ma'),
    ('fudge','call the judge'),
    ('fat','pet the cat'),
    ('fog','walk the dog'),
    ('fun',"say we're done")
]
start2="Someone better"

text1=''
for i in range(len(start1)):
    text1+=start1[i].capitalize() + "! "

text2=start2+" "
for i in range(len(rhymes)):
    text1+=rhymes[i][0].capitalize() + "! "
    text2+=rhymes[i][1]+"."
print(text1)
print(text2)