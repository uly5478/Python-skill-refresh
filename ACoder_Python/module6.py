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
    N = int(raw_input())
    Mi = map(int,raw_input().split() )

    i=0
    result=0
    while i<len(Mi):
        if Mi[i]<80:
            result+= 80-Mi[i]
        i+=1

    print result

if __name__ == '__main__':
    main()
