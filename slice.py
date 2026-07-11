import sys
if len(sys.argv) < 2:
    print("Too many Arguments")

for name in sys.argv[1:-4]:
    print('My name is ', name)

"""
when slice[1:]
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python slice.py Partha Sam Jerry Danny Thoufeeque Imman
My name is  Partha
My name is  Sam
My name is  Jerry
My name is  Danny
My name is  Thoufeeque
My name is  Imman

when slice[1:-4]
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python slice.py Partha Sam Jerry Danny Thoufeeque Imman
My name is  Partha
My name is  Sam

"""