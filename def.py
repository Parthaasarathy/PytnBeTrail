def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print("Hello", to)

main()
""" The code defines a main function that prompts the user for their name and then calls the hello function, 
passing the user's name as an argument. The hello function takes a parameter 'to' and 
prints a greeting message that includes the value of 'to'. When the main function is executed, 
it will ask for the user's name and greet them accordingly.
Example output:What's your name? Partha 
Hello Partha"""

def calc():
    x = float(input("Enter the Number: "))
    print("The sqaured of X is: ",square(x))

def square(n):
    return n**2

calc()
""" The code defines a function called calc that prompts the user to enter a number, 
converts it to a float, and then calls the square function with that number as an argument. 
The square function takes a parameter 'n' and returns the value of 'n' raised to the power of 2 (i.e., n squared). 
When the calc function is executed, it will ask for a number, calculate its square using the square function, 
and print the result. The sqaure can also be calculated using n*n, pow(n,2) instead of n**2.
Example output: Enter the Number: 5
The sqaured of X is:  25.0
"""
