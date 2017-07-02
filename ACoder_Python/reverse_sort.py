#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     22/05/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    A = int(raw_input())
    B = int(raw_input())
    C = int(raw_input())

    Mi = [A,B,C]

    Ni = sorted([A,B,C],reverse=True)

    i =0
    while i<len(Mi):
        j=0
        while Mi[i]!=Ni[j]:
            j+=1
        print j+1
        i+=1

if __name__ == '__main__':
    main()
