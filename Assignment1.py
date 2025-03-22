# Part 1 - Python Basics (Variables)

# Printing Name with escape sequences
print("My Name: Ali \nFather's Name: Ahmed \nDate of Birth: 01-01-2000")

# Small bio using variables
name = "Ali"
age = 24
city = "Lahore"
hobby = "Coding"
print("My name is", name, "I am", age, "years old and I live in", city, ". My hobby is", hobby, ".")

# Using all operators
x, y = 10, 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Comparison:", x > y)
print("Logical AND:", x > 5 and y < 5)
print("Bitwise AND:", x & y)

# Marks and Percentage Calculation
english = 85
islamiat = 90
maths = 80
total_marks = 300
obtained_marks = english + islamiat + maths
percentage = (obtained_marks / total_marks) * 100
print("Percentage:", percentage, "%")

# Part 2 - Conditional Statements

# Bonus Calculation
salary = int(input("Enter Salary: "))
service_years = int(input("Enter Years of Service: "))
if service_years > 5:
    print("Bonus:", salary * 0.05)
else:
    print("No Bonus")

# Voting Eligibility
age = int(input("Enter Age: "))
print("Eligible for voting" if age > 17 else "Not eligible")

# Even or Odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Divisibility by 7
num = int(input("Enter a number: "))
print("Divisible by 7" if num % 7 == 0 else "Not Divisible")

# Multiple of 5
num = int(input("Enter a number: "))
print("Hello" if num % 5 == 0 else "Bye")

# Last Digit of a Number
num = int(input("Enter a number: "))
print("Last Digit:", num % 10)

# Square or Rectangle
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
print("Square" if length == breadth else "Rectangle")

# Greatest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greatest:", max(a, b))

# Discount Calculation
quantity = int(input("Enter quantity: "))
total_cost = quantity * 100
total_cost -= total_cost * 0.1 if total_cost > 1000 else 0
print("Total Cost:", total_cost)

# Grading System
marks = int(input("Enter marks: "))
if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"
print("Grade:", grade)

# Attendance Check
classes_held = int(input("Enter total classes: "))
classes_attended = int(input("Enter attended classes: "))
attendance = (classes_attended / classes_held) * 100
print("Attendance:", attendance, "%")
print("Allowed" if attendance >= 75 else "Not Allowed")

# Attendance with Medical Reason
medical = input("Do you have a medical cause? (Y/N): ")
print("Allowed" if attendance >= 75 or medical == "Y" else "Not Allowed")

# Leap Year Check
year = int(input("Enter year: "))
print("Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year")

# Place of Service
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
marital_status = input("Married? (Y/N): ")
if gender == "F":
    print("Work in Urban Areas")
elif gender == "M" and 20 <= age <= 40:
    print("Can work anywhere")
elif gender == "M" and 40 <= age <= 60:
    print("Work in Urban Areas")
else:
    print("ERROR")

# Electricity Bill Calculation
units = int(input("Enter units: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)
print("Total Bill: Rs.", bill)

# Oldest and Youngest
age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))
print("Oldest:", max(age1, age2, age3))
print("Youngest:", min(age1, age2, age3))
