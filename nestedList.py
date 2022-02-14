
numbers = [1, 2, 3, 4, 5, 6]
newNumbers = [[1, 2, 3], [4, 5, 6]]

# index_1 = newNumbers[1]

# number_6 = index_1[2]

# number = newNumbers[1][2]
# print(number)
# print("--------------")
# for li in newNumbers:
#     for num in li:
#         print(num)
# print("--------------")

# copyList = [[print(l) for i in li] for li in newNumbers]
# # print(copyList)
generetedList = [num for num in range(1, 4)]
gereretedNestedList = [
    [newNum for newNum in range(1, 4)] for num in range(1, 4)]
print(generetedList)
print(gereretedNestedList)
 