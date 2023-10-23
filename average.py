# a program that calculates the average of a set of 3 numbers


def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# enter the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


avg = average(num1, num2, num3);

print("The average is: ", avg)