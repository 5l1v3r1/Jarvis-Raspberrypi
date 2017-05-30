# -*- coding:utf-8 -*-
from UNO import UNO
unotask = []
UNO = UNO()

class serTest():
    def __init__(self):
        pass

    def write(self,command):
        print "write:"+command
ser = serTest()

while True:
    UNO.monitor(ser)
    UNO.execute(ser, unotask)
