from django.db import models
from user.models import User

# Create your models here.
'邻接矩阵'


class MeetNum(models.Model):
    '遇见人的列表'
    friend = models.ManyToManyField(User, verbose_name='用户')
    distance = models.FloatField(verbose_name='距离')
    age = models.IntegerField(verbose_name='年龄')
    # gender = models.CharField(max_length=2, verbose_name='性别')
    site = models.CharField(max_length=100, null=True, verbose_name='相遇地点')
    meettime = models.DateTimeField(auto_now=True, verbose_name='相遇时间')
    meetcount = models.IntegerField(verbose_name='遇见编号')
    longitude = models.DecimalField(null=False, verbose_name='经度', max_digits=9, decimal_places=6)
    latitude = models.DecimalField(null=False, verbose_name='纬度', max_digits=8, decimal_places=6)

    class Meta:
        db_table = 'meetnum'


class MeetSite(models.Model):
    '相遇点的记录'
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    site = models.CharField(null=True, max_length=200, verbose_name='相遇地点')
    meettime = models.DateTimeField(auto_now_add=True, verbose_name='相遇时间')
    nums = models.IntegerField(verbose_name='相遇次数')

    class Meta:
        db_table = 'meetsite'


class MeetLike(models.Model):
    '喜欢人列表'
    user = models.ManyToManyField(User, verbose_name='用户')
    username = models.CharField(max_length=32, verbose_name='用户名')

    class Meta:
        db_table = 'meetlike'


class MeetUnlike(models.Model):
    '不喜欢人的列表'
    user = models.ManyToManyField(User, verbose_name='用户')
    username = models.CharField(max_length=32, verbose_name='用户名')
    count = models.IntegerField(verbose_name='不喜欢次数')
    gender = models.CharField(max_length=6, verbose_name="性别")

    class Meta:
        db_table = 'meetunlike'


class Count(models.Model):
    '总数量列表'
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    count = models.IntegerField(verbose_name='数量')

    class Meta:
        db_table = 'count'


class Version(models.Model):
    '更新版本'
    appName = models.CharField(max_length=10, verbose_name='项目名称')
    packageName = models.CharField(max_length=20, verbose_name='包名')
    versionCode = models.CharField(max_length=12, verbose_name='版本码')
    versionNumber = models.IntegerField(verbose_name='版本编号')
    fileUrl = models.CharField(max_length=100, verbose_name='文件地址')
    fileName = models.CharField(max_length=30, verbose_name='文件名字')
    updateTime = models.CharField(max_length=30, verbose_name='更新时间')
    versionContent = models.CharField(max_length=1024, verbose_name='版本内容')

    class Meta:
        db_table = 'version'
