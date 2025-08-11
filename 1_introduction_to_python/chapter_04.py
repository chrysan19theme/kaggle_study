#4.1
secret=4
guess=6
if guess<secret:
    print('too low')
elif guess>secret:
    print('too high')
else:
    print('just right')

#4.2
small=True
green=False
if small and green:
    print('pea')
elif small:
    print('cherry')
elif green:
    print('watermelon')
else:
    print('pumpkin')