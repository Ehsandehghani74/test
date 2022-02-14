# myNumber = [1, 2, 3, 4, 5, 6]
# print(myNumber[0])
# print(myNumber[1])
# print(myNumber[2])
# print(myNumber[3])
# print(myNumber[4])
# print(myNumber[5])
from msilib.schema import CompLocator
from operator import index


myColors = ["red", "blue", "green", "gray", "yellow", "orange", 2.6]

for color in myColors:
    if type(color) == str:
        print(f"the color is : {color}")
    else:
        print(f"{color} is not a color")
print('--------------------------------')

index = 0
while index < len(myColors):
    color = myColors[index]
    if type(color) == str:
         print(f"the color is : {color}")
    else:
        print(f"{color} is not a color")
    
    index += 1