#find majority element
#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

import sys

with open("user.out", 'w') as f:
    for line in sys.stdin:
        l = sorted(map(int, line.rstrip()[1:-1].split(',')))
        f.write(str(l[len(l) // 2]) + '\n')
exit(0)
