import colorama
from math import factorial, pow
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from hexalattice.hexalattice import *


def triangle():
    colorama.init()  # Starts scanning ouput streams for ansi and replaces with win32 calls if needed.
    #! Messing around with hexagons. Perhaps getting a triangle down.
    rows = int(input("Input number of rows: "))
    hex_centers, _ = create_hex_grid(n=rows+1, do_plot=True)
    print(hex_centers)
    plt.show()
    
    ##########
    for n in range(rows):
        

    colorama.deinit()  # Restores output streams functionality.


#Time & Space: O(N^2), O(N) : Modified GeeksForGeeks code
def generateNthRow(N):

    # nC0 = 1
    prev = 1
    row = str(prev) + " "

    for i in range(1, N + 1):

        # nCr = (nCr-1 * (n - r + 1))/r
        curr = (prev * (N - i + 1)) // i
        row = row + str(curr) + " "
        prev = curr
        
    return len(row)


triangle()
