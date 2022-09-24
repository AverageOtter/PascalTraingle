#This is a modification of code sourced from : https://nekrasovp.github.io/pascals-triangle.html

# simple Pascal's triangle realisation
# populated with Pascal's triangle rows give an infinite sequence of finite sequences
# this implementation support few printing styles

"""
Notes: 
-Formatting breaks down after 13 rows. 
-Color coding does not mess with spacing. 
-This algorithims population function runs in O(n^2)
"""


import math
from colorama import *

class PascalsTriangle():

    def __init__(self, rowcount):
        self.rowcount = rowcount
        self.pt = self._create()

    def _create(self):
        """Create an empty list and then append lists of 0s, each list one longer than the previous"""
        return [[0] * r for r in range(1, self.rowcount + 1)]

    def populate(self):
        """Populate an uninitialized list with actual values"""
        for r in range(0, len(self.pt)): # For each row 0 - n : n
            for c in range(0, len(self.pt[r])): # For each number in row r + 1 : r+1
                self.pt[r][c] = math.factorial(r) / (math.factorial(c) * math.factorial(r - c)) #O(n)/O(n^2)

    def print_centre(self):
        """Prints the triangle in a conventional centred format"""
        inset = int(((((len(self.pt) * 2) - 1) / 2) * 3))
        for r in range(0, len(self.pt)):
            print(" " * inset, end="")
            for c in range(0, len(self.pt[r])):
                if(int(self.pt[r][c] % multiple == 0)):
                    print(Fore.RED + '{:>3}   '.format(int(self.pt[r][c])), end="")
                else:
                    print(Fore.RESET + '{:>3}   '.format(int(self.pt[r][c])), end="")
            print()
            inset -= 3
        

rows = int(input("Input number of rows: "))
while True:
    multiple = int(input("Input the multiple to be highlighted (-1 for No): "))
    if multiple == 0:
        print("Whoops! That would've been a divide by 0 Error! Try Again!\n")
    else:
        break
        
values = str(input("Would you like to have values? y/n : "))
init()
triangle = PascalsTriangle(rows)
if(values.lower() == "y"):
    triangle.populate()
triangle.print_centre()
deinit()
