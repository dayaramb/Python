str3=[]
def interleave(str1,str2,result=None):
  if result is None:
    result=''
  if not str1 and not str2:
    str3.append(result)
  else:
    if str1:
      r1=result+str1[0]
      interleave(str1[1:],str2,r1)
    if str2:
      r2=result+str2[0]
      interleave(str1,str2[1:],r2)



interleave('AB','CD')
print "The string is:", str3
