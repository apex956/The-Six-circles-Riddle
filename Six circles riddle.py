"""
The riddle:
There are 16 items (circles) arranged in a four by four square matrix
Remove 6 of the items so that the number of remaining items on every row, column, and major diagonal, is even.

How many ways are there to select 6 items out of 16? The answer is "16 choose 6" which is 8008
So the code has to run over all 8008 combinations and for each one check all the conditions
detailed in the riddle (10 conditions).
Use an array from 0 to 15. Initially assign the value 1 to all the array elements.
For each of the 6 selected elements assign the value zero.
For each of the 8008 arrays, go over the 10 combinations (corresponding to rows, columns, diagonals)
add up the values of the four elements and select those arrays where all 10 results are an even number.
"""
import numpy as np
import tkinter as tk
from itertools import combinations


def check_if_even(num):
    """Check if the number is even"""
    if num % 2 == 0:
        return True
    else:
        return False


def check_for_even_number(items):
    """ Test if the number of circles (items) that are left  in all the rows, columns and major diagonals is even.
        If a circle is in place, the value is 1, otherwise it is 0 """

    # check the rows
    sum1 = items[0] + items[1] + items[2] + items[3]
    sum2 = items[4] + items[5] + items[6] + items[7]
    sum3 = items[8] + items[9] + items[10] + items[11]
    sum4 = items[12] + items[13] + items[14] + items[15]
    if check_if_even(sum1) is False or check_if_even(sum2) is False or \
            check_if_even(sum3) is False or check_if_even(sum4) is False:
        return False
    # check the columns
    sum1 = items[0] + items[4] + items[8] + items[12]
    sum2 = items[1] + items[5] + items[9] + items[13]
    sum3 = items[2] + items[6] + items[10] + items[14]
    sum4 = items[3] + items[7] + items[11] + items[15]
    if check_if_even(sum1) is False or check_if_even(sum2) is False or \
            check_if_even(sum3) is False or check_if_even(sum4) is False:
        return False

    # check the two major diagonals
    sum1 = items[0] + items[5] + items[10] + items[15]
    sum2 = items[3] + items[6] + items[9] + items[12]
    if check_if_even(sum1) is False or check_if_even(sum2) is False:
        return False
    return True

# 16 choose 6
array_of_zeros_combo = np.array(list(combinations(range(16), 6)))

print("Shape of array_of_zeros_combo: ", array_of_zeros_combo.shape)
num_rows, num_cols = array_of_zeros_combo.shape

# create an item list based on the indexes
num_solutions = 0
rslt_lst = []
for row in range(num_rows):  # loop over rows in array_of_zeros_combo
    tst_item = [1]*16  # start with a list of 16 1's
    for z_idx in array_of_zeros_combo[row]:
        tst_item[z_idx] = 0  # replace the 1's by zero's at the location of the index
    # test the sequences:
    test_result = check_for_even_number(tst_item)
    if test_result is True:
        num_solutions += 1
        print("Combination #", num_solutions)
        print(tst_item[0:4])
        print(tst_item[4:8])
        print(tst_item[8:12])
        print(tst_item[12:16])
        rslt_lst.append(tst_item)
print("Total number of solutions:", num_solutions)

window = tk.Tk()  # The root
window.title("Six Circles Removed")
window.geometry('900x1000')
window.resizable(False, False)
txt_font = "Helvetica 14"
solution_frame = []
for col in range(8):
    for row in range(8):
        fm_idx = 8*col+row
        solution_frame.append(tk.Frame(window, bg="black", relief='raise', bd=4))
        solution_frame[fm_idx].grid(column=col, row=row)
        tk.Label(solution_frame[fm_idx], text=str(rslt_lst[fm_idx][0:4]), font=txt_font).grid(column=0, row=0)
        tk.Label(solution_frame[fm_idx], text=str(rslt_lst[fm_idx][4:8]), font=txt_font).grid(column=0, row=1)
        tk.Label(solution_frame[fm_idx], text=str(rslt_lst[fm_idx][8:12]), font=txt_font).grid(column=0, row=2)
        tk.Label(solution_frame[fm_idx], text=str(rslt_lst[fm_idx][12:16]), font=txt_font).grid(column=0, row=3)

window.mainloop()
