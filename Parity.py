def main():
    x = int(input("Enter the Number X: "))
    if is_even(x):
        print("X is even")
    else:
        print("X is odd")
    
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
main()

"""We can also write the is_even function as
return n%2 == 0
this will return the boolean thus we will the same output
"""