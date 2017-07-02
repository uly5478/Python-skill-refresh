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
import sys
from sys import stdin

def main():
    #print "Hello"
    #print sys.version

    userinput = stdin.readline()
    a=int(userinput)
    userinput2 = stdin.readline()

    b=int(userinput2.split()[0])
    c=int(userinput2.split()[1])
    userinput3 = stdin.readline().strip('\n')
    print a+b+c,userinput3

    #pass

    # get a integer
    #a = int(raw_input())
    # get two integers separated with half-width break
    #b, c = map(int, raw_input().split())
    # get a string
    #s = raw_input()
    # output
    #print str(a+b+c) + " " + s




if __name__ == '__main__':
    main()
