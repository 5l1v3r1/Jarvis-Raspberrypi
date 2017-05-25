# -*- coding:utf-8 -*-
import os
import threading

def getPlugins(directory = 'background'+os.sep+'backgroundtasks'):
    files = os.listdir(directory)
    plugins = []
    for nameext in files:
        if nameext[-2:] == 'py' and nameext != '__init__.py':
            plugins.append(nameext.split('.',1)[0])
    return plugins



def setup(ser,config):
    '''
       ser是serial.Serial(port,baud,timeout=timeout)的实例
       这个函数主要用于启动一些自启动功能脚本
    '''
    plugins = getPlugins()
    threads=[]
    for plugin in plugins:
        exec('from backgroundtasks import ' + plugin)
        exec("tem_t=threading.Thread(target=" + plugin + ".main,args=(ser,config))")
        threads.append(tem_t)    
    
    for t in threads:
        t.setDaemon(True)
        t.start()
    # t.join()  ##用于等待线程终止


if __name__ == '__main__':
    d = 'backgroundtasks'
    files = os.listdir(d) 
    for f in files:
        print f
