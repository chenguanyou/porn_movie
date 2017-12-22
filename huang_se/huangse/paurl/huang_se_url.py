#conding=UTF-8
#By:陈冠佑
#QQ:1475348764
#Python3.6
import requests
#import huang_se_url_server
import huang_se_video
from bs4 import BeautifulSoup
url_database = []
i = 2 #从来第二页开始用来控制url的页数
x = 1 #用来控制打印提示是第N条数据
name = "黄色url.txt"
def zhua_huangse_url(urlls):
    global x
    global i
    global url_database
    while True:
        huang_se_url = urlls+"_%d.html"%i
        huang_se_url_get = requests.get(huang_se_url)
        huang_se_url_jiexi = BeautifulSoup(huang_se_url_get.content,"html5lib")
        huang_se_url_s = huang_se_url_jiexi.select("#content > div.clear > div > div.span-755 > div.clear > div > div > div > a")
        for huang_se_url_ss in huang_se_url_s:
            huang_se_url_data = {"url":huang_se_url_ss.get("href")}
            wanzheng_url_data = "http://www.04pcpc.com"+huang_se_url_data["url"]
            url_database.append(wanzheng_url_data)
            print("第%d条小黄片%s抓取成功！"%(x,wanzheng_url_data))
            huang_se_video.pa_huangse_xinxi(wanzheng_url_data)
            x+=1
            continue
        print("第",i,"页面！")
        i+=1
        #huang_se_url_server.Server_url(name,url_database)
    print("url采集结束！即将进行数据清洗》》》》》》》》》》》》")
