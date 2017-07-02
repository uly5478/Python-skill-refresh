#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     25/07/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    # get a integer
    N, M = map(int,raw_input().split() )

    R = []


    Place = []

    i = 0
    while i<N:
        Place.append(i+1)
        i+=1

    #print "Init",Place

    i = 0
    while i<M:
        Ri = int(raw_input())
        R.append(Ri)
        i+=1

    i = 0
    while i<M:
        writing = Place.pop(Place.index(R[i]))
        Place.insert(0,writing)
        #print R[i],writing,Place
        i+=1

    i = 0
    while i<N:
        print Place[i]
        i+=1

if __name__ == '__main__':
    main()
