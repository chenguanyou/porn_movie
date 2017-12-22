#conding=utf-8
#Django1.11.7
#Python3.6
#By:陈冠佑
#QQ:1475348764
import os
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator ,InvalidPage,EmptyPage,PageNotAnInteger #导入paginator实现分页功能，并且引入他的3个异常类型
from huangse.models import *
# Create your views here.

#获取全局配置
def view_setting(request):
    #huangse_title = huangse.objects.all().distinct().order_by('-id')#[:10]
    counts = huangse.objects.all().distinct().order_by('-id').count()  # [:10]
    sostr = souci.objects.order_by().last()
    hstitle = huangse.objects.filter(titles__contains=sostr).distinct()  # 获取标题
    shuliang = hstitle.count()
    #以下分页功能
    paginator = Paginator(hstitle,10)
    try:
        page = int(request.GET.get('p',1))
        hstitle = paginator.page(page)
    except (InvalidPage,EmptyPage,PageNotAnInteger):
        hstitle = paginator.page(1)
    # 以上分页功能
    TITLES = settings.TITLES
    return locals()

#视频数据同步数据库需要单独调用运行
def jin_ku():
    #hs_list = []
    print(os.getcwd())
    open_file = open('./huangse/paurl/黄色小视频-未处理.txt', 'r')
    du_file = eval(open_file.read())
    open_file.close()
    print(du_file[0])
    for url in du_file:
        huangse.objects.create(
            titles = url['title'],
            urls = url['url']
        )

#定义一个视频主页
def index(request):
    #jin_ku()#把数据放到数据库,我在这里做了放到数据库的操作，因为爬虫还是我之前写的，所有就直接来用了，需要有数据入库的时候，把这个注释去掉就好啦，当然你也可以在爬虫里面直接把数据存放在数据库
    if request.method == "POST":
        title = request.POST['title']
        souci.objects.create(titstr=title)
        hstitle = huangse.objects.filter(titles__contains=title).distinct()#获取标题
        paginator = Paginator(hstitle, 10)
        try:
            page = int(request.GET.get('p', 1))
            hstitle = paginator.page(page)
        except (InvalidPage, EmptyPage, PageNotAnInteger):
            hstitle = paginator.page(1)
    return render(request,'index.html',locals())

#播放页面
def tages(request):
    try:
        # 获取小黄片idd
        id = request.GET.get('id', None)
        url = request.GET.get('id',None)
        # 获取小黄片信息
        tages = huangse.objects.get(pk=id)
        tagurl = huangse.objects.all().values("urls").get(pk=id)
        #print(tagurl)
    except huangse.DoesNotExist:
        return render(request, 'tages.html', {'reason': '没有找到对应的车'})
    return render(request,'tages.html',locals())
