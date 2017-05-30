# -*- coding:utf-8 -*-
#main()不能有return,有我也没有处理
import urllib2,re,time
def finish(ser,w,wea):
    if wea=='':
        ser.write('play,152,$')
    else:
        dic={'多云转阴':'155','云':'156','小雨':'157','小雨转中雨':'158','小雨转阴':'159','雨转多云':'160','阴':'161','雨转晴':'162','晴转多云':'163','阵雨转多云':'164','暴雨':'165','阵雨转阴':'166','多云转晴':'167','雷阵雨':'168','小雨转多云':'169','雨转阴':'170','中雨转阴':'171','多云转小雨':'172','多云转中雨':'173','中雨':'174','暴雨转小雨':'175','多云':'176','中雨转小雨':'177','阵雨转小雨':'178','大雨转小雨':'179'}
        try:
            if w=='（明天）':
                ser.write('play,151,$')
            else:
                ser.write('play,150,$')
            time.sleep(2)#语音防重叠参数
            ser.write('play,'+dic[wea]+',$')
        except KeyError:
            ser.write('play,153,$')
            

def GetNowTime():
    return time.strftime("%H",time.localtime(time.time()))

def main(myparam):
    cityurl="http://www.weather.com.cn/weather/101270101.shtml"#请自行到中国天气网得到对应城市的URL
    #默认查询成都天气
    req=urllib2.Request(cityurl)
    fd=urllib2.urlopen(req)
    data=fd.read().split('\n')
    fd.close()
    t=GetNowTime()
    if int(t)>=17:#以下午5点为界限决定查询今天还是明天天气
        w='（明天）'
    else:
        w='（今天）'
    find=0
    wea=''
    for i in range(0,len(data)):
        d=data[i]
        if re.search(w,d)==None and find==0:
            continue
        else:
            find=1
        weather=re.search("class=\"wea\">(.*)</p>",d)
        if weather!=None:
            wea=weather.group(1)
            break
    finish(myparam.ser,w,wea)
            

if __name__=='__main__':
    cityurl="http://www.weather.com.cn/weather/101270101.shtml"#请自行到中国天气网得到对应城市的URL
    req=urllib2.Request(cityurl)
    fd=urllib2.urlopen(req)
    data=fd.read().split('\n')
    fd.close()
    t=GetNowTime()
    if int(t)>=17:#以下午5点为界限决定查询今天还是明天天气
        w='（明天）'
    else:
        w='（今天）'
    find=0
    for i in range(0,len(data)):
        d=data[i]
        if re.search(w,d)==None and find==0:
            continue
        else:
            find=1
        weather=re.search("class=\"wea\">(.*)</p>",d)
        if weather!=None:
            finish('dd',w,weather.group(1))
            break
            
            
                                

        

        
            
            
            
