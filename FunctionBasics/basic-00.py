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


question_2()