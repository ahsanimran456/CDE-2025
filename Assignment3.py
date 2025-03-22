# 1. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    print("Number of vowels:", count)

s = input("Enter a string: ")
count_vowels(s)


# 2. Count uppercase, lowercase, digits, and whitespace

def count_characters(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    digits = sum(1 for char in s if char.isdigit())
    spaces = sum(1 for char in s if char.isspace())
    print(f"Uppercase letters: {upper}\nLowercase letters: {lower}\nDigits: {digits}\nWhitespace characters: {spaces}")

s = input("Enter a string: ")
count_characters(s)


# 3. Swap first and last character

def swap_first_last(s):
    if len(s) > 1:
        s = s[-1] + s[1:-1] + s[0]
    print("New string:", s)

s = input("Enter a string: ")
swap_first_last(s)


# 4. Reverse the string

def reverse_string(s):
    print("Reversed string:", s[::-1])

s = input("Enter a string: ")
reverse_string(s)

# 5. Shift characters one position left

def shift_left(s):
    print("Shifted string:", s[1:] + s[0])

s = input("Enter a string: ")
shift_left(s)


# 6. Print initials without split()

def print_initials(name):
    initials = ""
    for i in range(len(name)):
        if i == 0 or name[i-1] == " ":
            initials += name[i].upper() + ". "
    print(initials.strip())

name = input("Enter full name: ")
print_initials(name)


# 7. Check if a string is a palindrome (without reverse())

def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            print("Not a palindrome")
            return
    print("Palindrome")

s = input("Enter a string: ")
is_palindrome(s)


# 8. Generate cyclic shifts

def cyclic_shifts(s):
    for i in range(len(s)):
        print(s[i:] + s[:i])

s = "SHIFT"
cyclic_shifts(s)


# 9. Password validation
def validate_password(password):
    if (len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password)):
        print("Password is valid")
    else:
        print("Invalid password")

password = input("Enter a password: ")
validate_password(password)

