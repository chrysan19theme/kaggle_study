#8.1
e2f=dict(dog='chien',cat='chat',walrus='morse')
print(e2f)

#8.2
print(e2f.get('walrus'))

#8,3
f2e=dict()
for eng,fr in e2f.items():
    f2e[fr]=eng
print(f2e)

#8.4
print(f2e['chien'])

#8.5
print(set(e2f.keys()))

#8.6
life={'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':{},'emus':{}},'plants':{},'other':{}}

#8.7
print(life.keys())

#8.8
print(life['animals'].keys())

#8.9
print(life['animals']['cats'])

#8.10
squares={number : number ** 2 for number in range(10)}
print(squares)

#8.11
odd={number for number in range(10) if number % 2 ==1}
print(odd)

#8.12
keys=('optimist','pessimist','troll')
values=('The glass is half full','The glass is half empty','How did you get a glass?')

dict1={}
for key,value in zip(keys,values):
    dict1[key]=value
print(dict1)

#8.13
titles=['Creature of Habit','Crewel Fate','Sharks on a plane']
plots=['A nun turns into a monster','A haunted yarn shop','Check your exits']
dict2={}
for key,value in zip(titles,plots):
    dict2[key]=value
print(dict2)