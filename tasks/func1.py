# -*- coding:utf-8 -*-
#提取学校重要新闻，并把结果放置桌面
import time
import urllib,urllib2
import re
import os
def GetMouDay():
    return time.strftime("%m-%d",time.localtime(time.time()))#注意权限

def limitation(pretime=7):#生成时间限，默认7天以内的
    time=GetMouDay().split('-')
    limtime=30*int(time[0])+int(time[1])-pretime
    return limtime

def JiaoWuChu(limtime,fi):
    url="http://www.jwc.uestc.edu.cn/"
    req=urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    req.add_header('Accept-Encoding','gzip, deflate')
    f=urllib2.urlopen(req)
    data=f.read().split('\n')
    f.close() 
    Lr='' 
    for i in xrange(0,len(data)):
        d=data[i]
        if re.search("div class=\"newInfo\" id=\"newInfo\"",d)!=None:
            #fi.write('\n')
            fi.write('>重要公告'+'\n')
            continue
        if re.search("<div class=\"hotInfo teachingTemplate\">",d)!=None:
            fi.write('\n')
            fi.write('>长期公告'+'\n')
            continue
        if re.search("id=\"module2\" class=\"teachingTemplate\">",d)!=None:
            fi.write('\n')
            fi.write('>教学管理(考试中心)公告'+'\n')
            continue
        if re.search("id=\"module3\" class=\"teachingTemplate\">",d)!=None:
            fi.write('\n')
            fi.write('>教学研究公告'+'\n')
            continue
        if re.search("id=\"module4\" class=\"teachingTemplate\">",d)!=None:
            fi.write('\n')
            fi.write('>实践教学(对外合作交流)公告'+'\n')
            continue
        if re.search("id=\"module5\" class=\"teachingTemplate\">",d)!=None:
            fi.write('\n')
            fi.write('>教学新闻'+'\n')
            continue
        if re.search("<div class=\"rightInfo\">",d)!=None:
            fi.write('\n')
            break
        m=re.search("title=\"(.*)\" target=\"_blank\">",d)
        if m!=None:
            Ahref=url+re.search("a href=\"(.*)\" title",d).group(1)
            Lr=m.group(1)+'  '+Ahref+'\n'
            continue
        t=re.search("class=\"teaching_time\">(.*)</span>",d)
        if t!=None:
            date=t.group(1).split('-')
            date=30*int(date[0])+int(date[1])
            if date>limtime:
                fi.write(t.group(1)+':'+Lr)
            continue

        
def DianGong(limtime,fi):
    url="http://www.ee.uestc.edu.cn"
    req=urllib2.Request(url)
    f=urllib2.urlopen(req)
    data=f.read().split('\n')
    f.close()
    
    jump=1
    for i in xrange(0,len(data)):
        d=data[i]
        #这段代码只有搜索到<div class="teaching">学生公告</div>才开始接下里的匹配
        if re.search("<div class=\"teaching\">",d)==None and jump==1:
            continue
        else:
            if jump==1:
                jump=0
                fi.write('\n电子信息工程学院--学生公告:\n')
        #到这里需要进行结束判断,发现<div class="menuMore">就结束循环
        if re.search("<div class=\"menuMore\">",d)!=None:
            break
            
        href=re.search("<a href=\"(.*)\">",d)
        if href!=None:
            Ahref=url+href.group(1).strip('\t')
            continue
        
        news=re.search("(.*)</p></a>",d)
        if news!=None:
            Lr=news.group(1).strip(' ').strip('\t')
            continue
        
        t=re.search("([0123456789 \t-]+)</span>",d)
        if t!=None:
            getdate=t.group(1).strip(' ').strip('\t')
            date=getdate.split('-')
            date=30*int(date[1])+int(date[2])
            if date>limtime:
                fi.write(getdate+' : '+Lr+' Link: '+Ahref+'\n')
            continue
        
      
  
def finish(ser):#给模块完成口令
    while True:
        try:
            ser.write('play,051,$')
        except:
            print "Something wrong in finish() of func1.py"#调试代码
            break
        else:
            break
        

def main(myparam=''):
    limtime=limitation(7)#设定什么时间才算最新新闻,这是一个数字型变量
    os.chdir(r'C:\Users\Administrator\Desktop')
    fi=open('SchoolInfo.txt','w')
    JiaoWuChu(limtime,fi)
    DianGong(limtime,fi)
    fi.close()
    finish(myparam.ser)
    
    
if __name__=='__main__':
    main()
