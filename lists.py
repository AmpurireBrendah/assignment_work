#Lists
#Store data.
# they are always mutable.
student_names=["Brendah", "Sandra","Phionah","Musimenta","Rahuman"] #strings
student_marks=[90,97,67,78,89] #integers
data=["Brendah",90, "Kamwokya"] #mixed

#Access the whole list
print(student_names, type(student_names))

#Accessing the list items
# Indexes
print(student_names[0])#first item
print(student_names[1])#second item
print(student_names[2])# third item
print(student_names[3])#fourth item
print(student_names[4])#fifth item

#Negative indexing
print(student_names[-5])#first item
print(student_names[-4])#second item
print(student_names[-3])#third item
print(student_names[-2])# fourth item
print(student_names[-1])# fifth item

#Adding an item to the list
#append()
student_names.append("Agnes")
print(student_names)

#At a particular position
student_names.insert(2,"Faith")
print(student_names)