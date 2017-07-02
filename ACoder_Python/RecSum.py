#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     12/07/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    K, L, M, N, P, Q, R, S = [-4,1,2,6,0,3,1,4]

    FirstRecX = M-K
    FirstRecY = N-L

    FirstRecSum = FirstRecX*FirstRecY

    SecondRecX = R-P
    SecondRecY = S-Q

    SecondRecSum = SecondRecX * SecondRecY

    InterRecSum = 0

    if M>P and S>L and N>S and R>M:
        #print "11111111"
        InterRecSum = (M-P)*(S-L)
    elif M>P and N>Q and Q>L and R>M:
        #print "222222"
        InterRecSum = (M-P)*(N-Q)
    elif R>K and S>L and L>Q:
        #print "333333"
        InterRecSum = (R-K)*(S-L)
    elif R>K and N>Q and S>N:
        #print "4444444"
        InterRecSum = (R-K)*(N-Q)



    print FirstRecSum , SecondRecSum,InterRecSum





if __name__ == '__main__':
    main()
