#爬取csdn博客
from urllib import request
import re
from bs4 import BeautifulSoup
import gzip
def getHtml(url):
    response = request.urlopen(url)
    data = response.read()
    s = BeautifulSoup(data,'lxml')
    return s
def getList(src):
    reg = re.compile(r'/article/details/')
    texts = src.find_all('a',href=reg)
    texts = str(texts)
    reg = re.compile(r'a href="(.*?)"')
    l = re.findall(reg, texts)
    l1= set()
    for val in l:
        if val not in l1:
            l1.add(val)
    return l1

def getArticle(src):
    id = 0
    for val in src:
        html = getHtml(val)
        #reg = re.compile(r'/article/details/')
        texts = html.find_all('div',class_='markdown_views')
        texts = re.sub(r'<.*?>',' ',str(texts))
        texts = re.sub(r'\n','\n',str(texts))
        filename=str(id)+'.txt'
        t = str(texts)
        #print(t)
        with open(filename,'w') as f:
            f.write(t)
        id += 1
    return 0

url = "https://blog.csdn.net/ww1473345713"
src = getHtml(url)
l = getList(src)
getArticle(l)






