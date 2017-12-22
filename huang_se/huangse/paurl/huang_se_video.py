#conding=utf-8
#By:陈冠佑
#QQ:1475348764
#Python3.6
#爬取黄色url内的小黄片数据
import pandas
import requests
import huang_se_url_server
from bs4 import BeautifulSoup
name = "黄色小视频-未处理.txt"
video_database = []
def pa_huangse_xinxi(huangse_video_url):
    global video_database
    #huangse_video_url = "http://www.07xxoo.com/video/2017-12/29813.html"
    huangse_video_url_get = requests.get(huangse_video_url)
    huangse_video_url_jiexi = BeautifulSoup(huangse_video_url_get.content,"html5lib")
    huangse_video_url_jiexi_title = huangse_video_url_jiexi.select("title") #获取小黄片视频的名称
    huangse_video_url_jiexi_url = str(huangse_video_url_jiexi)
    video = huangse_video_url_jiexi_url.rfind("video=[\"")
    mp4 = huangse_video_url_jiexi_url.rfind(".mp4")
    huangse_video = str(huangse_video_url_jiexi_url[video:mp4] + ".mp4")
    huangse_video1 = huangse_video.rfind("h")
    huangse_video3 = huangse_video[huangse_video1:] #获取到黄色小视频的url
    for huangse_video_url_jiexi_titles , huangse_video3s in zip(huangse_video_url_jiexi_title , huangse_video3):
        video_data = {
            "title":huangse_video_url_jiexi_titles.get_text(),
            "url":huangse_video3
        }
        s1 = video_data["title"].rfind("-49")
        video_datas = video_data["title"][:s1]
        url_datas = video_data["url"]
        sudata_s = {
            "title":video_datas,
            "url":url_datas
        }
        print(sudata_s)
        video_database.append(sudata_s)
    huang_se_url_server.Server_url(name,video_database)

#pa_huangse_xinxi("http://www.07xxoo.com/video/2017-12/29813.html")
if __name__ == "__main__":
    s = pandas.DataFrame(video_database)
    #s.head(10)
    print(s)

