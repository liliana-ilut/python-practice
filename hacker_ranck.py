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