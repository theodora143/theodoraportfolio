
from random import *


#Create the list of words you want to choose from.
babynames = ["Issac", "Genovia","Lilac", "Ruby", "Kent", "Beau", "Geniva", "Genesis", "Geniyah"]

#Generates a random integer.
x = randint(0, len(babynames)-1)
y = randint(0, len(babynames)-1)

print(babynames[x])
print(babynames[y])
