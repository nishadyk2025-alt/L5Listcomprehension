grades = {"student1":65, "student 2":70, "student3":93, "student4":42, "student5":89}
total = 0
for marks in grades.values():
    total += marks
average = total/5
print("average of class:", average)
topper = max(grades.values())
Worst_performer = min(grades.values())
for name, marks in grades.items():
    if marks == topper:
        print("topper: ", topper, name)
    if marks == Worst_performer:
        print("worst scorer: ", Worst_performer, name)
searchname= input("give studentname")
grades.get(searchname)
print(searchname, marks)


