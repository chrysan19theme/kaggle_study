#9.1

def good():
    return ['Harry','Ron','Hermione']

#9.2



get_odds=(number for number in range(10) if number % 2 ==1)
for number,i in zip(get_odds,range(1,10)):
    if i ==3:
        print(number)

#9.3

def test(func):
    def new_function(*args,**kwargs):
        print('start')
        result=func(*args,**kwargs)
        print('end')
        return result
    return new_function

@test
def count(str,target):
    c=0
    for s in str:
        if s == target:
            c+=1
    return c

count('dwoeifhio','d')

#9.4
class OopsException(Exception):
    pass

try:
    raise OopsException('error')
except OopsException as err:
    print('Caught an oops',err)

#9.5
gen = (number for number in range(10))

for number in gen:
    print('Got',str(number))