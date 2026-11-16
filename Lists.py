# aaj khatam krenge:

# lists:

friend = ["ali", "ahmed", "bilal", "umer", "hassan"]

# print(friend[0])  # Output: ali
for i in range(0, len(friend)):
    print(friend[i])


print(friend[0:5:2])  # Output: ['ali', 'bilal', 'hassan']

# list functions:

friend.append("usman")  # adds one element to the end of the list
print(friend)  # Output: ['ali', 'ahmed', 'bilal', 'umer', 'hassan', 'usman']

friend.extend(["zain", "faizan"])  # adds multiple elements to the end of the list

friend.insert(0, "umer")  # adds an element at a specific index

print(friend)  # Output: ['umer', 'ali','ahmed', 'bilal', 'umer', 'hassan', 'usman', 'zain', 'faizan']

friend.remove("umer")
friend.pop()  # removes the last element from the list

lucky_numbers = [3,12,6,72,54,43]
lucky_numbers.sort()  # Output: None (sort() modifies the list in place and returns None)

print(lucky_numbers)  # Output: [3, 6, 12, 43, 54, 72]



