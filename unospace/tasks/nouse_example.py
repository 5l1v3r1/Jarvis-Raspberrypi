# -*- coding:utf-8 -*-
def ASR_output(ser, command):
    while True:
        try:
            ser.write(command)
        except:
            pass
        else:
            break
            
def main(ser, command, parameters):
    '''
    ser是 ASR串口对象
    command是ASR执行语言指令
    parameters是UNO传递回来的可读返回指令参数部分，格式xxx,xxx,xx......
    '''
    pass