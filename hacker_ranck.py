# QUESTION 1:
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# SOLUTION 1:
# if __name__ == '__main__':
a = int(input())
b = int(input())
    
first_line = a + b
print(first_line)
    
second_line = a - b
print(second_line)
    
third_line = a * b
print(third_line)

# QUESTION 2:
# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example


# The result of the integer division .
# The result of the float division is .
# Print:

# 0
# 0.6
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# Output Format

# Print the two lines as described above.

# SOLUTION 2:
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    
first_line = a // b
print(first_line)

second_line = a / b
print(second_line)

# QUESTION 3:
# The provided code stub reads and integer, , from STDIN(Standard input). For all non-negative integers i <n , print i^2 .

# Example
# n=3

# The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each number on a separate line.
# SOLUTION 3:
if __name__ == '__main__':
    n = int(input())
    
    for n in range (0,n):
        square = n ** 2
        print(square)

# QUESTION 4:
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
# SOLUTION 4:

def is_leap(year):
    leap = False
    if ((year % 4 == 0) and (year % 100 !=0) or (year % 400 ==0)):
        leap = True
                
    # Write your logic here
    
    return leap

year = int(input())

# QUESTION 5:
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following: 123...n
# Note that "n" represents the consecutive values in between.
# SOLUTION 5:
if __name__ == '__main__':
    n = int(input())
    for n in range (1, n+1):
         print(n, end= "") 