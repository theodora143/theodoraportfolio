
from random import *


#Create the list of words you want to choose from.
sides = ["wings", "fries","mozzarella", "soup", "salad", "potato skins", "garlic bread"]
main = ["spaguetti","lasagna","burger","chilli fries","pizza","calamari","lobster"]
desserts = ["mousse","ice cream cake", "muffins", "mint ice cream", "brownies","sherbert","cheesecake"]

meal = ""
#Generates a random integer.
x = randint(0, len(sides)-1)
y = randint(0, len(main)-1)
d = randint(0, len(desserts)-1)

meal += sides[x] + " " + main[y] + " " + desserts[d]

print("your random name is " + meal)
