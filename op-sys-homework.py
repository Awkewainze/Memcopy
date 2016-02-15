# Dylan Walseth (walsethd)

import sys
import mmap
import os

number_diffs = 0

def main():
    if(check_args()):
        line_number = 1
        with open(sys.argv[1], "r") as f1:
            with open(sys.argv[2], "r") as f2:
                map1 = mmap.mmap(f1.fileno(), 0, access=mmap.ACCESS_READ)
                map2 = mmap.mmap(f2.fileno(), 0, access=mmap.ACCESS_READ)
                continue_reading = True
                while continue_reading:
                    line1 = map1.readline()
                    line2 = map2.readline()
                    continue_reading = compare_line(line1, line2, line_number)
                    line_number += 1
                global number_diffs
                print("There " + ("was 1 difference" if number_diffs == 1 else ("were " + str(number_diffs) + " differences")))

"""
Checks to see if arugments provided are valid files
Returns boolean if files are valid and should run
"""
def check_args():
    if(len(sys.argv) != 3):
        print("Expected 2 args, 'python compare.py <file1> <file2>'")
        return False
    if(not os.path.isfile(sys.argv[1])):
        print(sys.argv[1] + " is not a valid file")
        return False
    if(not os.path.isfile(sys.argv[2])):
        print(sys.argv[2] + " is not a valid file")
        return False
    return True

"""
Compares 2 lines and prints them if they are different
Returns boolean whether the program should continue reading lines
"""
def compare_line(line1, line2, line_number):
    global number_diffs
    if(line1 == "" or line2 == ""):
        if(line1 == "" and line2 == ""):
            print("Finished comparing files")
            return False
        if(line1 == ""):
            print(str(sys.argv[1]) + " ended unexpectingly (Before the other file was on it's final line)")
            return False
        if(line2 == ""):
            print(str(sys.argv[2]) + " ended unexpectingly (Before the other file was on it's final line)")
            return False
    if(line1 != line2):
        number_diffs += 1
        print("Line " + str(line_number) + ":")
        print("\t"+line1.strip())
        print("\t"+line2.strip())
    return True

main()
