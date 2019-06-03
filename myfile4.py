# # # # Case 1 : Accessing the items
# this_list = ["apple","banana","cherry"]
# print(this_list)                    # Ans : ['apple', 'banana', 'cherry']
# print(this_list[0])                 # Ans : apple

# # # # Case 2: Add
# this_list = ["apple","banana","cherry"]
# this_list.append("mango")
# print(this_list)                    # Ans : ['apple', 'banana', 'cherry', 'mango']
#
#
# this_list = ["apple","banana","cherry"]
# this_list.insert(2, "thenga")
# print(this_list)                    # Ans : ['apple', 'banana', 'thenga', 'cherry']
#
# # Adding duplicate
# this_list = ["apple","banana","cherry"]
# this_list.insert(2, "banana")
# print(this_list)                    # Ans : ['apple', 'banana', 'banana', 'cherry']

# # # # Case 3: Remove
# this_list = ["apple","banana","cherry"]
# this_list.remove("banana")
# print(this_list)                    # Ans : ['apple', 'cherry']
#
# this_list = ["apple","banana","cherry"]
# this_list.pop()
# print(this_list)                    # Ans : ['apple', 'banana']
#
#
# this_list = ["apple","banana","cherry"]
# this_list.pop(0)
# print(this_list)                    # Ans : ['banana', 'cherry']
#
#
# # # # Case 4: Change the value
# this_list = ["apple","banana","cherry"]
# this_list [1] = "chakka"
# print(this_list)                    # Ans : ['apple', 'chakka', 'cherry']

# # # Changing the value to a duplicate value
# # this_list = ["apple","banana","cherry"]
# # this_list [2] = "banana"
# # print(this_list)                    # Ans : ['apple', 'banana', 'banana']
#
# # Case 5: Finding the length
# # this_list = ["apple","banana","cherry"]
# # print(len(this_list))                   # Ans : 3
#
# # Case 6: Sorting
# this_list = [2,3,1,5,4]
# this_list.sort()
# print(this_list)

# # Case 7: Reversing
# # this_list = ["cherry","apple","banana"]
# # this_list.reverse()
# # print(this_list)
#
# # Case 8: counting the occurrence of an item in trhe list
# this_list = ["banana", "cherry","apple","banana","banana"]
# print(this_list.count("banana"))      # Ans : 3


# Case 9: Max and Min
# this_list = [1, 2, 3, 4, 5]
# print(max(this_list))                   # Ans : 5
# print(min(this_list))                   # Ans : 1

#
# # Case 10: Deleting
# this_list = ["apple","banana","cherry"]
# del this_list[0]
# print(this_list)                           # Ans :  ['banana', 'cherry']

#
# this_list = ["apple","banana","cherry"]
# del this_list
# print(this_list)                          # Ans : NameError: name 'this_list' is not defined

# # Case 11: Clearing the list
# this_list = ["apple","banana","cherry"]
# this_list.clear()
# print(this_list)                             # Ans : []

# # Case 12: Concatinatination
# this_list = ["apple","banana","cherry"]
# that_list = ["chakka","manga","thenga"]
# my_list = this_list + that_list
# print(my_list)                              # Ans: ['apple', 'banana', 'cherry', 'chakka', 'manga', 'thenga']


# # Case 13: loops --> For loop
# this_list = ["apple","banana","cherry"]
#
# for x in this_list:
#     print(x)


# Case 14: finding the existance  -->  if -- else
# this_list = ["apple","banana","cherry"]
# if "apple" in this_list:
#     print("apple is there in the fruit list")