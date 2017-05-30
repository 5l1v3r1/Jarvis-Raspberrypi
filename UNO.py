# -*- coding:utf-8 -*-
import threading
import Queue
import serial
import time
from unospace import returned_config
from unospace.tasks import *

def getUNOData(readable_instruction_Queue,unoser):
    error_time = 0
    while 1:
        try:
            readable_instruction = unoser.readline()
            if not readable_instruction:
                readable_instruction_Queue.put(readable_instruction)
        except:
            if error_time >= 5:
                break
            else:
                time.sleep(2)
                continue




class UNO(object):
    def __init__(self):
        if platform.platform().lower().find('windows')!=-1:
            port = 'com6'
        else:
            port='/dev/ttyACM0'
        self.unoser = serial.Serial(port,9600,timeout = 1)
        self.unoser.flushInput()#flush input buffer, discarding all its contents
        self.unoser.flushOnput()#flush output buffer, aborting current output#and discard all that is in buffer

        self.readable_instruction_Queue = Queue.Queue()
        threads=[]
        t = threading.Thread(target=getUNOData,args=(self.readable_instruction_Queue,self.unoser,))
        threads.append(t)
        for t in threads:
            t.setDaemon(True)
            t.start()

        self.returned_config = returned_config.main()

    def _find_in_config(self, instruction):
        for i in xrange(0,len(self.returned_config)):
            if self.returned_config[i][0] == instruction:
                return self.returned_config[i]
        return []

    def monitor(self,ser):
        while not self.readable_instruction_Queue.empty():
            readable_instruction = readable_instruction_Queue.get()
            nonparam_readable_instruction,parameters = readable_instruction.split('-')
            # 这里必须保证UNO返回的可读指令有且只有一个-
            config_detial = self._find_in_config(nonparam_readable_instruction) 
            #例子:['shake', 'play,191,$', 'shake']
            if not config_detial:
                eval(config_detial[2]+".main"+"(ser, "+config_detial[1]+", "+parameters+")")


    def execute(self,ser,unotask):
        pass
