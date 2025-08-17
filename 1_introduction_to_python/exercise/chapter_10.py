#10.1
class Thing:
    pass

example=Thing()

print(Thing)
print(example)

#10.2
class Thing2:
    letters='abc'

print(Thing2.letters)

#10.3
class Thing3:
    pass

example3=Thing3()
example3.letters='xyz'

print(example3.letters)

#10.4
class Element:
    def __init__(self,name,symbol,number):
        self.__name=name
        self.__symbol=symbol
        self.__number=number
    def __str__(self):
        return f'name:{self.__name},symbol:{self.__symbol},number:{self.__number}'
    
    @property
    def name(self):
        return self.__name
    
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number

example4=Element('Hydrogen','H',1)

#10.5
dict5=dict(name='Hydrogen',symbol='H',number=1)
hydrogen=Element(**dict5)
#hydrogen.dump()

#10.6
print(hydrogen)
#print(str(hydrogen))

#10.8
print(hydrogen.name)

#10.9
class Bear:
    def eats(self):
        return ('berries')

class Rabbit:
    def eats(self):
        return ('clover')
    
class Octothorpe:
    def eats(self):
        return ('campers')

#10.10
class Laser:
    def does(self):
        return ('disintegrate')

class Claw:
    def does(self):
        return ('crush')
    
class SmartPhone:
    def does(self):
        return ('ring')
    
class Robot:
    def __init__(self):
        self.laser=Laser()
        self.claw=Claw()
        self.smart_phone=SmartPhone()
