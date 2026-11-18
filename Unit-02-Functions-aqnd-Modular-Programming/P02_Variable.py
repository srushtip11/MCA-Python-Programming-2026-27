def calculate(name, *args, **kwargs):
    total = sum(args)
    average = total / len(args)
    highest = max(args)

    return total, average, highest

name = "Rahul"
total, average, highest = calculate(
    name, 80, 90, 85,
    roll_no=101, class_name="MCA"
)

print("Student Name:", name)
print("Roll Number: 101")
print("Class: MCA")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)