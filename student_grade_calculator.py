student1=(input("Enter the student's name: "))
marks1=int(input("Enter the student's marks: "))

student2=(input("Enter the student's name: "))
marks2=int(input("Enter the student's marks: "))

record={}
record.update({student1:marks1})
record.update({student2:marks2})

print(record)
if marks1 >=90 and marks1 <=100:
    print(student1 , ": excellent")
elif marks1 >=75 and marks1 <=89:
    print(student1 ,": good")
elif marks1 >=50 and marks1 <=74:
    print(student1 ,": average")
else:
    print(student1 ,": needs improvement")


if marks2 >=90 and marks2 <=100:
    print(student2 , ": excellent")
elif marks2 >=75 and marks2 <=89:
    print(student2 , ": good")
elif marks2 >=50 and marks2 <=74:
    print(student2 ,": average")
else:
    print(student2 ,": needs improvement")