# Question 1:
#    Ask user to input two numbers, print the smallest number out.

def question_1():
    def smaller_number(a, b):
        if a < b:
            return a
        else:
            return b


    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("The smaller number is:", smaller_number(num1, num2))


# Question 2:
#    Ask user to input three numbers, print the smallest number out&&
def question_2():
    def smaller_number(a, b, c):
        if a < b and a < c:
            return a
        elif b < a and b < c:
            return b
        else:
            return c


    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    print("The smaller number is:", smaller_number(num1, num2, num3))


# Question 3:
#    Can you use the first smaller_number funcion to implement question_2

# Question 3:
# Use the first smaller_number function to implement question_2

def question_3():

    # Original smaller_number function (two parameters)
    def smaller_number(a, b):
        if a < b:
            return a
        else:
            return b

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    # Step 1: smallest of first two
    smallest_first_two = smaller_number(num1, num2)

    # Step 2: compare with third
    smallest_all = smaller_number(smallest_first_two, num3)

    print("The smaller number is:", smallest_all)

# Question 4:
#    Given a single integer n, print out the factorial of n.

def factorial_program():
    n = int(input("Enter an integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    result = 1
    for i in range(1, n + 1):
        result = result * i

    print("The factorial of", n, "is", result)

# Question 5:
#     Solve question 4 with recursive approach.
def factorial_program_recursive():
    # no AI generated code.
    

def factorial(n):
    if n == 0:          # base case (stops recursion)
        return 1
    else: 
        return n * factorial(n - 1)   # function calls itself


def question_4():
    n = int(input("Enter an integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("The factorial of", n, "is", factorial(n))


question_4()
