import sys
import mmap
import os

def main():
    file1, file2 = check_args()
    with open(STAT_FILE, "r+b") as f:
        map = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        for line in iter(map.readline, ""):
            compare = line == ""

def check_args():
    if(len(sys.argv) != 3):
        print("Expected 2 args, 'python compare.py <file1> <file2>'")
        return False
    try:
        pass
        # file1 = open(sys.argv[0])
    except Exception as e:
        print("Invalid file(s) provided")
    return "good"

# main()

print check_args()
