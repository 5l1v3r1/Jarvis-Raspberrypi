# -*- coding:utf-8 -*-
#main()不能有return,有我也没有处理
#这个脚本执行久坐提醒功能
import subprocess,threading,time
Sittime=3600#配置多少秒后提醒

def finish(ser):
    while True:
        try:
            ser.write('play,055,$')
        except:
            print "Something wrong in finish() of func1.py"#调试代码
            break
        else:
            break

def Clock(sit,ser):#接受秒为单位的数字时间比如,Sittime
    time.sleep(sit)
    while True:
        try:
            ser.write('play,180,$')
        except:
            pass
        else:
            break

def main(ser):
    t=threading.Thread(target=Clock,args=(Sittime,ser,))
    t.setDaemon(True)
    t.start()
    finish(ser)
    

if __name__=='__main__':
    pass
