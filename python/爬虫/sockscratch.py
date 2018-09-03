import urllib
import urllib.request
import re

def getpage():
    data= urllib.request.urlopen(path).read().decode("gbk");
    return data;

def runpage(min,max):
    for page in range(min,max):
        html="http://quote.stockstar.com/stock/sha_3_1_"+str(page)+".html"
        print(html)

runpage(1,40)
