me = {
    "name": "Ehsan",
    "familiy": "dehghani",
    "gmail": "ehsandehghani123@gmail.com"
}
print(me)

# me.pop("name")
# me.popitem()
# print(me)

second = {
    "age": 50,
    "name": "milad"
}
second.update(me)
print(second)

second["name"] = "sara"

print(second)