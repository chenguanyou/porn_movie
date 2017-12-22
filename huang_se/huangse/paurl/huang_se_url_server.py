from django import *
#conding=utf-8
#By:陈冠佑
#QQ:1475348764
#Python3.6
#保存抓取的列表内的url
def Server_url(name,huanse_url):
    huang_se_url_open = open(name,"w")
    huang_se_url_xie = huang_se_url_open.write(str(huanse_url))
    huang_se_url_open.close()

#清洗未处理的数据
def Server_xi(name,huanse_url):
    huang_se_url_open = open(name,"a")
    huang_se_url_xie = huang_se_url_open.write(str(huanse_url)+"\n"+"\n")
    huang_se_url_open.close()
