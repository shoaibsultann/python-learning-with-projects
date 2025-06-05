# Q2: Write a program to accept marks of 6 students and display them in a sorted manner.

Marks = []

firstStudent = int(input("Enter first student maths marks: "))
Marks.append(firstStudent)

secondStudent = int(input("Enter second student maths marks: "))
Marks.append(secondStudent)

thirdStudent = int(input("Enter third student maths marks: "))
Marks.append(thirdStudent)

fouthStudent = int(input("Enter fouth student maths marks: "))
Marks.append(fouthStudent)

fifthStudent = int(input("Enter fifth student maths marks: "))
Marks.append(fifthStudent)

sixthStudent = int(input("Enter sixth student maths marks: "))
Marks.append(sixthStudent)

Marks.sort()

all_students_maths_marks = f"Here is the maths marks sorted list: {Marks}"
print(all_students_maths_marks)
