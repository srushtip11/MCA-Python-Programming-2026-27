import arithmetic

from arithmetic import add, subtract

import student

print("Addition:", arithmetic.add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", arithmetic.multiply(10, 5))
print("Division:", arithmetic.divide(10, 5))

print("\nStudent Information:")
student.student_details()
student.student_result()