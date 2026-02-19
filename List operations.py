# How can we append inside the list
from itertools import count

from decorator import append
from dill import extend

Name = ["Vinod", "Stephen", "George", "Mohammed"]
Name.append("Shafeeulla")
print(Name)

#How can we extend the list
Names = ["Shahid"]
Name.extend(Names)
print(Name)

#Remove item from the list
Name.remove("Vinod")
print(Name)

#Pop item from the list
Name.pop()
print(Name)

#How to insert element at a specific index
Name.insert(2,"Md")
print(Name)

#To count specific elements in a list
No = Name.count("Md")
print(No)

#To remove element from a list
Name.remove("Md")
print(Name)

#To pop element from the list
Name.pop(2)
print(Name)

#How to sort elements in a list
Name.sort()
print(Name)

#How to reverse elements in a list
Name.reverse()
print(Name)

#Membership operators
print('Stephen' in Name)
