# -*- coding:utf-8 -*-
import time
"""
08:00 主人，该起床活动了
11:30 主人，该去吃午饭了
17:05 主人，该去吃晚饭了
23:00 主人，夜深了该休息了
"""
def convert(hm):
    second = (int(hm[0])*60 + int(hm[1])) * 60
    return second

def timejudge(hourminute):
    key_time = [['08','00'],
                ['11','30'],
                ['17','05'],
                ['23','00']]
    commands = ['play,170,$'
                'play,171,$'
                'play,172,$'
                'play,173,$']
    for i in xrange(len(key_time)):
        if hourminute == key_time[i]:
            return 0,commands[i]
        else:
            current_num = convert(hourminute)
            key_num = convert(key_time[i])
            if current_num < key_num:
                return (key_num - current_num),''
    return convert(key_time[0]),''

def timehandle(current):
    return current.split()[3].split(":")[0:2] #"['09', '30']"

def execute(ser, command):
    while True:
        try:
            ser.write(command)
        except:
            pass
        else:
            break

def main(ser,config):
    while True:
        current = time.ctime()
        hourminute = timehandle(current)
        sleep_time,command = timejudge(hourminute)
        if not sleep_time:
            execute(ser, command)
        else:
            time.sleep(sleep_time)

    
        
if __name__=='__main__':
    convert(['08','30'])
        
            
            

            
        
        
    
    
    
    
    
    
