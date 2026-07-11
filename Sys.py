import sys
if len(sys.argv) < 2:  #argv = argument vector
    sys.exit("Too few Arguments")
elif len(sys.argv) > 2:
    sys.exit("Too Many arguments")

print("Hello, my Name is ", sys.argv[1])

"""
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python sys.py Parthasarathy
Hello, my Name is  Parthasarathy
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python Sys.py 
Too few Arguments
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python Sys.py Parthasarathy S
Too Many arguments
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python Sys.py "Parthasarathy S"
Hello, my Name is  Parthasarathy S 
"""