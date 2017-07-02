#-------------------------------------------------------------------------------
# Name:        module2
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
    a = int(raw_input())
    # split two integers separated with half-width break
    #b, c = map(int, [a[0],a[1]])
    b = raw_input()

    #print a,b
    c = b.strip('abc')
    #print "remain:",len(c)
    if len(c) != 0 :
        print "-1"
        return

    accessary="b"
    step=0
    while len(b) > len(accessary):
        step+=1
        if step % 3 ==1:
            accessary='a'+accessary+'c'
        elif step %3 ==2:
            accessary='c'+accessary+'a'
        else:
            accessary='b'+accessary+'b'
        #print"IN LOOP:",step,accessary

    if accessary==b:
        print step
    else:
        print "-1"

if __name__ == '__main__':
    main()
