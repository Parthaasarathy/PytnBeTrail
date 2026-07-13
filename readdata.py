names = []
"""
This script reads names from a text file named 'readdata.txt', stores them in a list,
sorts the names alphabetically, and prints a greeting message for each name.

Functions:
- None

Variables:
- names: A list to store the names read from the file.

File Requirements:
- 'readdata.txt': A text file located in the same directory as this script. Each line
    in the file should contain one name.

Usage:
- Ensure 'readdata.txt' exists in the same directory as this script and contains the
    names to be processed.
- Run the script to print a greeting for each name in alphabetical order.
"""

with open("readdata.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")