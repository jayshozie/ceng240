grades = []
average = 0

while True:
    new_grade = eval(input("Please enter the next grade : "))

    if new_grade < 0:
        break

    grades.append(new_grade)

grades.sort()
grades.pop(-1)  # Delete last element
grades.pop(0)  # Delete first element

if len(grades) > 0:
    average = sum(grades) / len(grades)

print(f"Grades : {grades}")
print(f"Average : {average:.2f}%")
