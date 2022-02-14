from audioop import reverse
from itertools import count
from operator import index
from textwrap import indent


myCourses = ["Pythone", "Kotlin", "Ionic", "Pythone", "JQuery", "Vuejs", "Pythone"]
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # index_kotlin = myCourses.index("Kotlin")
# # index_Ionic = myCourses.index("Ionic")
# index_Pythone = myCourses.index("Pythone", 1, 5)

# print(index_Pythone) 

# count 

# numberOfpython = myCourses.count("Pythone")
# print(numberOfpython)

# reverse

# print(myNumbers)
# myNumbers.reverse()
# print(myNumbers) 
unOrderedNumbers = [5, 9, 6, 3, 18, 75, 1]
print(unOrderedNumbers)
unOrderedNumbers.sort()
print(unOrderedNumbers)