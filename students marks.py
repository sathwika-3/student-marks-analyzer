students={}
n=int(input("enter number of students:"))
for i in range(n):
    name=str(input("enter student name:"))
    marks=int(input("enter marks:"))
    students[name]=marks
print("\nStudent Results")
for name,marks in students.items():
    if marks>=90:
        grade="A"
    elif marks>=75:
        grade="B"
    elif marks>=50:
        grade="C"
    else:
        grade="Fail"
    print(name,marks,grade)