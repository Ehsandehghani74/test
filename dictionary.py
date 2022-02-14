import numbers
from typing import ItemsView


myNumbers = [1, 2, 3, 4, 5, 6]
name = ["Ehsan", "Shahruz", "Hamid", "Khosro"]
test = ["python", True, 5, [4, 5, 6]]

myDictionary = {
    "name": "Item 1",
    "count": 3,
    "price": 2500,
    3: "test"
}

myDictionary_2 = dict(name="new Dictionery", age=25)
print(myDictionary_2)

myShoppingCart = [{"name": "python", "price": "free"},
                  {"name": "kotlin", "price": 2500}
                  ]
print(myDictionary)

print(myDictionary_2["name"])

me = {
    "name": "Ehsan",
    "family": "dehghani",
    "age": 26
}

# print(me.values())
# print(me.keys(:))
for item in me.items():
    print(item)

    print("test")
    print("test")
