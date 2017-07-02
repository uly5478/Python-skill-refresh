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
    S = raw_input()
    N = int(raw_input())
    srr = []
    for i in S:
        srr+=i

    #Operate = []
    i=0
    while i<N:
        #Operate.append(map(int,raw_input().split() ))
        L,R = map(int,raw_input().split())

        j=0

        while L+j<R-j:

            temp = srr[L-1+j]
            srr[L-1+j] = srr[R-1-j]
            srr[R-1-j] = temp
            j+=1

        i+=1

    #print srr
    print ''.join(srr)
if __name__ == '__main__':
    main()
