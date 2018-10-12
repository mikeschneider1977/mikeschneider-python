from random import *

winOrDie = []
for i in range(0, 20):
    winOrDie.append('live')



winLocation = randint(0, 19)
dieLocation = randint(0, 19)


print(winLocation)
print(dieLocation)

winOrDie[dieLocation] = 'die'
winOrDie[winLocation] = 'win'

print(winOrDie)

