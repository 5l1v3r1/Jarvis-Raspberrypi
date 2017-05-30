# -*- coding:utf-8 -*-
#main()不能有return,有我也没有处理
import random
songs=6#请修改你SD卡里歌曲wav文件的数目

def finish(ser,music):
    while True:
        try:
            ser.write('play,'+music+',$')
        except:
            print "Something wrong in finish() of func9.py"#调试代码
            break
        else:
            break

def main(myparam):
    r=random.randint(0,songs-1)#生成0~songs-1中的随机数(含二边)
    music=str(100+r)#101之类的字符串
    finish(myparam.ser,music)
    

if __name__=='__main__':
    a=0
    b=0
    c=0
    d=0
    for i in xrange(0,1000):
        r=random.randint(0,3)
        #print type(r)#int
        if r==0:
            a+=1
        if r==1:
            b+=1
        if r==2:
            c+=1
        if r==3:
            d+=1
    print "0 has showed up "+str(a)+' times'
    print "1 has showed up "+str(b)+' times'
    print "2 has showed up "+str(c)+' times'
    print "3 has showed up "+str(d)+' times'
