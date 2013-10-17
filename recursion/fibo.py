#!/usr/bin/python
#Printing the fibonacci series: (Provided first term, second term and count)
def fibo(n1,n2,count):
  n3=n1+n2
  print n3
  (n1,n2)=(n2,n3)
  if count:
    fibo(n1,n2,count-1)



fibo(1,2,5)
