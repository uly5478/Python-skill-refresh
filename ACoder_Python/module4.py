#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     16/05/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    A, B = map(int,raw_input().split() )
    #print A,B,A-B
    A1=A
    B1=B

    if A<900:
        A1+=(9-int(A/100))*100
    elif A<990:
        A1+=(9-int((A-900)/10))*10
    elif A!=999:
        A1+=9-(A-990)

    if B>=200:
        B1= 100+B%100
    elif B>=110:
        B1= 100 + B % 10
    else:
        B1= 100

    #print "!!!!!",A1,B1

    if A1-A > B-B1:
        print A1-B
    else:
        print A-B1


    #print A-B

if __name__ == '__main__':
    main()
