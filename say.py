import sys
from sayings import hello
from sayings import goodbye

if len(sys.argv) == 2:
    #hello(sys.argv[1])
    goodbye(sys.argv[1])

"""
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python say.py Partha 
hello, Partha
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python say.py Partha
Goodbye, Partha
"""