#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uly
#
# Created:     14/05/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
     # get a integer
    #a = int(raw_input())
    # split two integers separated with half-width break
    R, C, K = map(int,raw_input().split() )
    #print R,C,K

    b = int(raw_input())
    i=b
    sugar=[]
    while i>0:
        i-=1
        Ri,Cj=map(int,raw_input().split() )
        #print "Sugar:",Ri,Cj
        sugar.append([Ri,Cj])

    #print "END LOOP1"
    #print len(sugar)
    count=0
    i,j=1,1
    while i<=R:
        j=1
        while j<=C:
            n=0
            gotSugar=0
            while n<len(sugar):
                #print "!!!!",n
                Ri,Cj= sugar[n]
                #Cj= sugar[n][1]
                if Ri==i :
                    gotSugar+=1
                elif Cj ==j:
                    gotSugar+=1
                n+=1
            #print i,j,"GotSugar:",gotSugar
            if gotSugar==K:
                count+=1
            j+=1
        i+=1

    #pass
    print count




if __name__ == '__main__':
    main()
