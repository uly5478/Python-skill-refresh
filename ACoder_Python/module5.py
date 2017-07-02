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
    #A, B = map(int,raw_input().split() )
    K = int(raw_input())

    X,Y=0,0
    Steps = [[0,0]]

    Si=raw_input()
    i = 0
    while i<K:
        if Si[i] == 'R':
            X+=1
            while [X,Y] in Steps:
                X+=1
            #print "R",X,Y
        elif Si[i] == 'L':
            X-=1
            while [X,Y] in Steps:
                X-=1
            #print "L",X,Y
        elif Si[i] == 'U':
            Y+=1
            while [X,Y] in Steps:
                Y+=1
            #print "U",X,Y
        elif Si[i] == 'D':
            Y-=1
            while [X,Y] in Steps:
                Y-=1
            #print "D",X,Y
        Steps.append([X,Y])
        i+=1

    #print Steps
    print X,Y



if __name__ == '__main__':
    main()
