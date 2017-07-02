#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      uly
#
# Created:     11/07/2015
# Copyright:   (c) uly 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    # get a integer
    N = int(raw_input())


    R = []

    i = 0
    while i<N-1:
        Ri = int(raw_input())
        R.append(Ri)
        i+=1

    #salary =  []

    salary = [[] for x in range(N)]

    i = N-1
    while i>=0:
        #calculate mysalary
        if salary[i] == []:
            mysalary = 1
        else:
            #print "!!!!!!!!"
            mysalary = max(salary[i])+min(salary[i])+1
        #append mysalary to boss
        salary[R[i-1]-1].append(mysalary)
        #print salary
        i-=1

    #print N,R,salary,mysalary
    print mysalary


if __name__ == '__main__':
    main()
