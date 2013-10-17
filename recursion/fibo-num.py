#!/usr/bin/python
def fibo(n1,n2,count):
  if count:
    n3=n1+n2
    print n3
    (n1,n2)=(n2,n3)
    fibo(n1,n2,count-1)


fibo(0,1,5)
