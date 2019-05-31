from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    """
    用户表
    """
    uuid = models.CharField(max_length=32, verbose_name='用户ID')
    username = models.CharField(max_length=20, unique=True, null=False, blank=True, verbose_name="姓名")
    password = models.CharField(max_length=255, verbose_name="密码")
    age = models.DateField(null=False, blank=True, verbose_name="出生年月")
    # GENDER = (
    #     ("male", "男"),
    #     ("female", "女")
    # )
    # gender = models.CharField(max_length=6, choices=GENDER, default="female",
    #                           verbose_name="性别")
    # CONSTELLATION = (
    #     (1, "白羊座"),
    #     (2, "金牛座"),
    #     (3, "双子座"),
    #     (4, "巨蟹座"),
    #     (5, "狮子座"),
    #     (6, "处女座"),
    #     (7, "天秤座"),
    #     (8, "天蝎座"),
    #     (9, "射手座"),
    #     (10, "摩羯座"),
    #     (11, "水瓶座"),
    #     (12, "双鱼座"),
    # )
    # constellation = models.IntegerField(choices=CONSTELLATION, null=False, verbose_name='星座')
    # mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    # account = models.CharField(max_length=24, null=False, verbose_name="账号")
    # scope = models.CharField(max_length=124, null=False, verbose_name="地区")
    # signature = models.CharField(max_length=255, null=False, blank=True, verbose_name="个性签名")
    longitude = models.DecimalField(null=False, verbose_name='经度', max_digits=9, decimal_places=6)
    latitude = models.DecimalField(null=False, verbose_name='纬度', max_digits=8, decimal_places=6)
    # friend = models.ManyToManyField('self')


    class Meta:
        db_table = 'user'


class Phono(models.Model):
    """
    相册
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="用户")
    phono = models.ImageField(upload_to='upload', verbose_name="照片")
    default_display = models.BooleanField(default=True, verbose_name="默认显示")
    IMG_TYPE = (
        (1, "头像"),
        (2, "相册"),
        (3, "说说"),
    )
    phono_type = models.IntegerField(choices=IMG_TYPE, verbose_name='图片类型')

    class Meta:
        db_table = 'phono'


class Lable(models.Model):
    """
    标签
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="用户")
    LABLE_CHOICES = (
        (1, '运动'),
        (2, '日记'),
        (3, '电影'),
        (4, '格斗'),
        (5, '篮球'),
        (6, '篮球'),
        (7, '旅游'),
    )
    lable = models.IntegerField(choices=LABLE_CHOICES, verbose_name='标签')

    class Meta:
        db_table = 'lable'


class Relationship(models.Model):
    """
    好友关系
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE,  related_name="用户A")
    relation = models.ForeignKey('User', on_delete=models.CASCADE,  related_name="用户B")
    is_friends = models.BooleanField(default=False, verbose_name="是否是好友")

    class Meta:
        db_table = 'relationship'


# class User_Settings(models.Model):
#     """
#     设置
#     """
#     settings_id = models.IntegerField(verbose_name="设置ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     inform_method = models.CharField(max_length=32, verbose_name="消息通知")
#     hint_method = models.CharField(max_length=32, verbose_name="提示方式")
#     user = models.OneToOneField('User', on_delete=True, verbose_name="用户")
#
#     class Meta:
#         db_table = 'user_settings'
#
#
# class Feedback(models.Model):
#     """
#     意见反馈
#     """
#     feedback_id = models.IntegerField(verbose_name="反馈ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     content = models.TextField(null=True, blank=True, verbose_name="反馈内容")
#     content_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="问题")
#     user = models.ForeignKey('User', on_delete=True, verbose_name="用户")
#
#     class Meta:
#         db_table = 'feedback'
#
#
# class Dynamic_Talk(models.Model):
#     """
#     动态
#     """
#     dynamic_id = models.IntegerField(verbose_name="动态ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     content = models.TextField(null=True, blank=True, verbose_name="动态内容")
#     dynamic_add = models.CharField(max_length=255, null=True, blank=True, verbose_name="发布动态地址")
#     user = models.ForeignKey('User', on_delete=True, verbose_name="用户")
#     user_image = models.ForeignKey('User_Image', on_delete=True, verbose_name="定位地址")
#
#     class Meta:
#         db_table = 'dynamic_talk'
#
#
# class Comment_Like(models.Model):
#     """
#     评论和点赞
#     """
#     comment_id = models.IntegerField(verbose_name="评论ID")
#     dynamic_id = models.IntegerField(verbose_name="动态ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     content = models.TextField(null=True, blank=True, verbose_name="动态内容")
#     like = models.BooleanField(default=True, verbose_name="是否点赞")
#     user = models.ForeignKey('User', on_delete=True, verbose_name="用户")
#     dynamic_talk = models.ForeignKey('Dynamic_Talk', on_delete=True, verbose_name="动态")



# class User_Settings(models.Model):
#     """
#     设置
#     """
#     settings_id = models.IntegerField(verbose_name="设置ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     inform_method = models.CharField(max_length=32, verbose_name="消息通知")
#     hint_method = models.CharField(max_length=32, verbose_name="提示方式")
#     user = models.OneToOneField('User', on_delete=True, verbose_name="用户")
#
#     class Meta:
#         db_table = 'user_settings'
#
#
# class Feedback(models.Model):
#     """
#     意见反馈
#     """
#     feedback_id = models.IntegerField(verbose_name="反馈ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     content = models.TextField(null=True, blank=True, verbose_name="反馈内容")
#     content_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="问题")
#     user = models.ForeignKey('User', on_delete=True, verbose_name="用户")
#
#     class Meta:
#         db_table = 'feedback'
#
#
# class Dynamic_Talk(models.Model):
#     """
#     动态
#     """
#     dynamic_id = models.IntegerField(verbose_name="动态ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     content = models.TextField(null=True, blank=True, verbose_name="动态内容")
#     dynamic_add = models.CharField(max_length=255, null=True, blank=True, verbose_name="发布动态地址")
#     user = models.ForeignKey('User', on_delete=True, verbose_name="用户")
#     user_image = models.ForeignKey('User_Image', on_delete=True, verbose_name="定位地址")
#
#     class Meta:
#         db_table = 'dynamic_talk'
#
#
# class Comment_Like(models.Model):
#     """
#     评论和点赞
#     """
#     comment_id = models.IntegerField(verbose_name="评论ID")
#     dynamic_id = models.IntegerField(verbose_name="动态ID")
#     user_id = models.IntegerField(verbose_name="用户ID")
#     content = models.TextField(null=True, blank=True, verbose_name="动态内容")
#     like = models.BooleanField(default=True, verbose_name="是否点赞")
#     user = models.ForeignKey('User', on_delete=True, verbose_name="用户")
#     dynamic_talk = models.ForeignKey('Dynamic_Talk', on_delete=True, verbose_name="动态")
