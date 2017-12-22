from django.db import models

# Create your models here.
#创建黄色小视频的数据模型
class huangse(models.Model):
    titles = models.CharField(max_length=600,verbose_name="标题名称")
    urls = models.URLField(max_length=1200,verbose_name="片地址")

    class Meta:
        verbose_name = '视频名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.titles

class souci(models.Model):
    titstr = models.CharField(max_length=200,verbose_name="搜索关键词")

    def __str__(self):
        return self.titstr

