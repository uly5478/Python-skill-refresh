#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     23/05/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    N = int(raw_input())

    i=0
    MeatPut=[]
    MeatOut=[]
    while i<N:
        #Operate.append(map(int,raw_input().split() ))
        S,T = map(int,raw_input().split())
        #Meat.append([S,T])
        MeatPut.append(S)
        MeatOut.append(T)
        i+=1

    Grill = []

    time = 1

    LastTime = sorted(MeatOut,reverse=True)[0]

    Meatidx = 0

    while time<=LastTime:

        if Meatidx < len(MeatPut) and time == MeatPut[Meatidx]:
            Grill.append(Meatidx)
            print "MeatIn",Meatidx+1
            Meatidx+=1

        outidx = 0
        moreStart=0
        countidx=0
        count=[]
        while countidx < len(MeatOut):
            count.append(0)
            countidx+=1

        while outidx<len(MeatOut):
            if time == MeatOut[outidx]:
                print "meatOut",outidx+1
                if len(Grill)>=2:
                    print "MORE 2"
                    moreStart=1
                if moreStart ==1:
                    print "&&&&&&&&&"
                    for onGrill in Grill:
                        print "((((",count[onGrill]
                        count[onGrill] += 1
                        print "*****",onGrill
                Grill.remove(outidx)
                if len(Grill)== 0:
                    print "Grill EMPTY"
                    moreStart = 0
            outidx+=1


        print "Time:",time,Grill
        time+=1



    print MeatPut
    print MeatOut
    print LastTime
    print "Count",count
    print "END"

if __name__ == '__main__':
    main()
