x = int(input("Enter the Number X: "))
y = int(input("Enter the Number Y: "))
if(x==y):
    print("X and Y are equal")
elif(x>y):
    print("X is greater than Y")
else:
    print("Y is greater than X")

""" The code prompts the user to enter two numbers, X and Y, and then compares them using conditional statements.
- If X is equal to Y, it prints "X and Y are equal"""

x = int(input("Enter the Number X: "))
y = int(input("Enter the Number Y: "))
if(x<y or x>y):
    print("X and Y are not equal")
else:
    print("X and Y are equal")

""" The code prompts the user to enter two numbers, X and Y, and then compares them using a conditional statement.
Example output: Enter the Number X: 5
Enter the Number Y: 10
X and Y are not equal"""