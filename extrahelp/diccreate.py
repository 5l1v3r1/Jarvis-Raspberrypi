# -*- coding:utf-8 -*-
def addWord(theIndex,word,pagenumber): #存在就在基础上加入列表，不存在就新建个字典key
  theIndex.setdefault(word, pagenumber)
  
def N10to16_2(n):#把一个10进制数转换为2位16进制数的字符串格式
  if n<1 or n>255:
    return -1
  if n<16:
      return '0'+hex(n)[2:]
  else:
      return hex(n)[2:]

def taskdic(number):
  d={}
  for i in xrange(1,number+1):
    addWord(d,N10to16_2(i),'func'+str(i)+'.main(myparam)')
  return d

if __name__=='__main__':
  dic=taskdic(10)
  print dic
