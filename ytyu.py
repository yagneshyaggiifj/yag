def myfun(string,fun,n):
    print string
    print n
    fun(string,n)
def exploder(string,n):
    for n in range(0,n):
        print string
string=raw_input("enter the string")
n=int (input("enter num of times"))
myfun(string,exploder,n)
