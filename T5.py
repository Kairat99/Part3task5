#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    new_s1 = s1.replace(' ','')
    new_s2 = s2.replace(' ','')
    for index in range(len(new_s1)):
        if new_s1[index] in new_s2:
            result = 'YES'
            break
        else:
            result = 'NO'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
