#!/usr/bin/python
def fact(num):
  if num==0:
    return 1
  else:
    return num*fact(num-1)


def main():
  n=raw_input("Enter a num to find fact:")
  print "The factorial is:",fact(int(n))



if __name__=="__main__":
  main()
