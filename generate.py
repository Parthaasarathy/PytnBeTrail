#from random import choice --> allows us to explicitly import the particular funtion from the module 
#we use import to access the libraries
#we will be using the pip to access the packages will do the pip install on the command lines

import random
coin = random.choice(['heads', 'tails', 'Nothing'])
print(coin)
number = random.randint(1,54)
print(number)

#cards = random.shuffle(['King','Queen', 'Jack', 'Heart', 'Spade', 'Ace', 'Clover'])
#if we use like this it will throw the error 
#Traceback (most recent call last):
#  File "/Users/parthasarathysethuraman/Desktop/PythonTrail/generate.py", line 9, in <module>
#    for card in cards:
  #                ^^^^^
#TypeError: 'NoneType' object is not iterable

cards = ['King','Queen', 'Jack', 'Heart', 'Spade', 'Ace', 'Clover']
random.shuffle(cards)

for card in cards:
    print(card)
