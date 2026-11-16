name = "harsh"
age = 20
student_enrolled = True


print(type(name))
print(type(age))
print(type(student_enrolled))

age = "222"
age

print("=======================")
print(int(age)+10)

print("=======================")
print("=======================")
print("=======================")

number_1 = 3

if number_1 > 0:
    print("positive")
else:
    print("negative")    



for i in range(51):
    print(i)

print("==========while loop=============")

j=0

while j < 50+1:
    print(j)
    j=j+1



print("=======================")
print("=======================")
print("=======================")

names = "harsh"
for i in range(len(names)):
    print(names[i])

i =0
n = len(names)
j= n-1


names = list(names)
while i < n and j>=0:
    if(i==j):
        break
    temp = names[i]
    names[i] = names[j]
    names[j] = temp
    i+=1
    j-=1

print(names)    


print("=======================")
print("=======================")
print("=======================")


list_of_numbers = [1,2,3,4,5,6,7,8,9]

for i in range(len(list_of_numbers)-1, -1, -2):
    print(list_of_numbers[i])


list_of_numbers.append(10)
list_of_numbers.remove(3)

print(list_of_numbers)
print(list_of_numbers[0:5])

print("=======================")
print("=======================")
print("=======================")



tuples_of_numbers=(1,2,3,4,5,6,7,8,9)


print("this is tuples")
for i in range(len(tuples_of_numbers)-1, -1, -2):
    print(tuples_of_numbers[i])

# tuples_of_numbers[0] = 10   #tuples are immutable this will give 



