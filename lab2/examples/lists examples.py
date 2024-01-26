#example 1
mylist = ["apple", "banana", "cherry"]

#example 2
thislist = ["apple", "banana", "cherry"]
print(thislist)

#example 3
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#example 4
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#example 5
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#example 6
list1 = ["abc", 34, True, 40, "male"]

#example 7
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#example 8
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



#Access List Items

#example 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#example 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#example 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#example 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#example 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#example 6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#example 7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#Change List Items

#example 1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#example 3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#example 4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#example 5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items

#example 1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example 2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#example 3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#example 4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List Items

#example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#example 2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#example 3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example 4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#example 5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example 6
thislist = ["apple", "banana", "cherry"]
del thislist[0]

#example 7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) 

#loop lists

#example 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#example 2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#example 3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#example 4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

