# -*- coding:utf-8 -*-
import time
def main():
    # 可读返回指令 ser执行命令 处理任务脚本名(unosapce.tasks下的py文件名) #解释
    # attention：这里添加后请在tasks文件夹下写好处理任务脚本，并在音频文件\UNOmonitor语音\说明.txt里添加
    #语音对应关系即可
    config_detials = '''
    discover_people play,190,$ discover_people #对应UNO人体监测模块发现有人靠近
    shake play,191,$ shake  #对应UNO震动模块探测到震动
    blaze play,192,$ blaze #对应火焰传感器
    '''
    config = []
    for c in config_detials.split('\n'):
        c = c.strip()
        if not c:
            continue
        c = c.split()
        # print c
        config.append([c[0],c[1],c[2]])
        time.sleep(0.5)
    return config  #config是一个嵌套列表