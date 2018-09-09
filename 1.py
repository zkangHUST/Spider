#coding=utf-8
from urllib import request 
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    #url open打开网页
    page = request.urlopen(url)  
    html = page.read() #read()方法用于读取URL上的数据
    html = str(html)
    return html
    
def getHtmlList(html):
    reg = r'<a href="(/bizhi/bing_v48967/pic_.+?\.html)"'
    imgre = re.compile(reg)
    htmllist = re.findall(imgre,html)
    l = set()
    for i in range(len(htmllist)):
        #网页地址是相对路径，需要添加域名
        htmllist[i] = 'http://www.ivsky.com' + htmllist[i]
        if htmllist[i] not in l:
            l.add(htmllist[i])
    return l
def getImage(htmllist):
    i = 0
    for key in htmllist:
        html = getHtml(key)
        html = str(html)
        if (getImg(html, i) == 0):
            print("%s download success"%i)
        else: 
            print("%s download failed" %i)
        i+=1
def showProcessBar(a,b,c):  
    '''''回调函数 
    a:已经下载的数据块 
    b:数据块的大小 
    c:远程文件的大小 
    '''  
    percent=100.0*a*b/c  
    if percent > 100:  
        percent = 100  
    #显示下载进度
    print ('[downloading:] %.2f%%' % percent)  
def getImg(html,id):
    #分析网页，提取图片地址
    reg = r'<img id="imgis" src=\\\'(http://.+?\.jpg)'
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)     
    try:
        request.urlretrieve(imglist[0],'.\spider\data\\bing\%d.jpg'%id, showProcessBar)
        #print("%s download success"%x)
        return 0
    except :
        return -1



url = "http://www.ivsky.com/bizhi/bing_t2824/"
h = getHtml(url)
l= getHtmlList(h)
getImage(l)
 