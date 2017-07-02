#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     11/07/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def main():

    # get a integer
    N = int(raw_input())

    #half = int(a/2);
    R = []
    #print "aaaa",half;
    i = 0
    while i<N:
        Ri = int(raw_input())
        R.append(Ri)
        i+=1

    R.sort(reverse=True)

    Result = 0;

    i=0
    while i<N:
        if i+1<N:
            Result+=math.pow(R[i],2)-math.pow(R[i+1],2)
        else:
            Result+=math.pow(R[i],2)
        i+=2


    print Result*math.pi;



if __name__ == '__main__':
    main()
