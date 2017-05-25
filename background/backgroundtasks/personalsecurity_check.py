# -*- coding:utf-8 -*-
"""
如果主人在足够长的时间内都没有从语音接收端接收到任何消息，那么视为主人遇到未知的危险，将进行安全报警
"""
import time
from personalsecurity_alert import alert

def execute(ser, command):
    while True:
        try:
            ser.write(command)
        except:
            pass
        else:
            break

def play_alert(ser):
    command = 'play,185,$'  # 主人，为了确保您的安全，请对我下达你好或者其他命令
    execute(ser,command)

def main(ser,config):
    enough_time = 24 * 60 * 60
    extend_time = 5 * 60
    alert_time = enough_time + extend_time
    silent_time = 0
    while True:
        if config[0] == 1:
            silent_time = 0
            config[0] = 0
        else:
            if(silent_time < enough_time):
                sleep_time = 3600
                time.sleep(sleep_time)
                silent_time = silent_time + sleep_time
            else:
                if(silent_time < alert_time):
                    play_alert(ser)
                    time.sleep(extend_time)
                    silent_time = silent_time + extend_time
                else:
                    alert.alert(ser)
                    time.sleep(5*60) #每隔5分钟一次警报



        
                
        
if __name__=='__main__':
    pass