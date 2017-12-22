#conding=utf-8
#Python3.6
#By:陈冠佑
#QQ:1475348764
#主方法
import huang_se_url
import huang_se_url_open
list_url = "http://www.06pcpc.com/diao/se28"#用来存储小黄片的url列表
print("*"*60)
print("              请先爬取url，在爬取url内的视频地址，在洗数据        ")
print("*"*60)
tishi_guest = input("1：爬取url，2：爬取url里面的视频地址，3：清洗数据，请输入您要爬取的内容：")
if tishi_guest == "1":
    huang_se_url.zhua_huangse_url(list_url)
elif tishi_guest == "2":
    huang_se_url_open.open_xi()
elif tishi_guest == "3":
    huang_se_url_open.open_xixi()