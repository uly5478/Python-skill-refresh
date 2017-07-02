#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      uly
#
# Created:     11/07/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    X, Y = map(int,raw_input().split() )
    K = int(raw_input())

    if Y>K:
        Y-=K
        X+=K
    else:
        KX = Y
        KY = K - KX
        X = X - KY + KX

    print X



if __name__ == '__main__':
    main()
