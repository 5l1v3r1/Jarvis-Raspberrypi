# -*- coding:utf-8 -*-
import time

def execute(ser, command):
    while True:
        try:
            ser.write(command)
        except:
            pass
        else:
            break

def main(ser,config):
    sedentary_time =  3600 #秒
    while True:
        time.sleep(sedentary_time)
        command = "play,180,$"
        execute(ser, command)
            
        
if __name__=='__main__':
    pass