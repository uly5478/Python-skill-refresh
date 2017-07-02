#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      uly
#
# Created:     11/07/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(A):
    N = len(A)
    total = sum(A)
    lefts = 0
    for p, value in enumerate(A):
        partial = total - value
        if partial % 2 == 0 and lefts == (partial / 2) and 0 <= p < N:
            return p
        lefts += value
    return -1

if __name__ == '__main__':
    A= [-1, 3, -4, 5, 1, -6, 2, 1]
    print main(A)
