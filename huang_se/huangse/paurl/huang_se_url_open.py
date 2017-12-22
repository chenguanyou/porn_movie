#coding=utf-8
#By:陈冠佑
#QQ:1475348764
#Python3.6
#读取url内的信息
import huang_se_video
import huang_se_url_server
i = 0
name = "千万小黄片数据.txt"
def open_xi():
    global i
    xi_url = open("黄色url.txt","r")
    xi_url_du = eval(xi_url.read())
    xi_url.close()
    while i < len(xi_url_du):
        huang_se_video.pa_huangse_xinxi(xi_url_du[i])
        i+=1

#洗未处理的数据在保存
def open_xixi():
    global i
    shuji_s = ""
    xixi_url = open("黄色小视频-未处理.txt","r")
    xi_url_du = eval(xixi_url.read())
    for shuju in xi_url_du:
        shuju1 = str("片名：%s      片地址：%s"%(shuju["title"],shuju["url"]))
        huang_se_url_server.Server_xi(name,shuju1)
        print(shuju1)