from django.shortcuts import render

# Create your views here.
import datetime
import re
import uuid
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from user.models import User, Phono, Lable, Relationship
from utils.tenxunyun import TengXun, Random_verify
from user.age_age import CalculateAge


# 注册用户
def register(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        verify = request.POST.get('verify')
        user = User()
        try:
            mobile_re = '^1[3456789]\d{9}$'
            if not re.match(mobile_re, mobile):
                return JsonResponse({'code': -1, 'msg': '请输入正确手机号'})
            # if verify != request.session[mobile]:
            #     return JsonResponse({'code': -1, 'msg': '短信验证未通过'})
            user.password = make_password(password)
            uuid_id = str(uuid.uuid4()).replace('-', '')[:11]
            User.objects.create(mobile=mobile, password=password, uuid=uuid_id)
        except Exception as e:
            print(e)
            return JsonResponse({'code': -1, 'msg': '注册失败'})
        return JsonResponse({'code': -1, 'msg': '注册成功'})


def detail_user(request):
    if request.method == 'POST':
        # user_id head_portrait
        pk = int(request.POST.get('user_id', 0))
        head_portrait = request.FILES.get('head_portrait')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        scope = request.POST.get('scope')
        signature = request.POST.get('signature')
        try:
            age = CalculateAge(birthday)
            user = User.objects.get(pk=pk)
            user.username = username
            user.gender = gender
            user.age = age
            user.scope = scope
            user.signature = signature
            user.save()
            Phono(user=user, phono=head_portrait, phono_type="头像").save()
        except Exception as e:
            print(e)
            return JsonResponse({'code': -1, 'msg': '未获取到该用户'})
        return JsonResponse({'code': 200, 'msg': '完善信息成功！'})


# 计算星座
def get_constellation(month, date):
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手", "摩羯")
    if date < dates[month - 1]:
        return constellations[month - 1]
    else:
        return constellations[month]


print(get_constellation(8, 23))


def add_label(request):
    # label:  '1,2,3'
    if request.method == 'POST':
        pk = int(request.POST.get('user_id', 0))
        label = request.POST.get('label')
        # 如果len(label) == 0,那么则说明label是空字符串即是label = ''我们就将label_list = [],以逗号分隔字符串
        label_list = [] if len(label) == 0 else list(label.split(','))
        try:
            user = User.objects.get(pk=pk)
            # [1, 2, 3]s
            [Lable(user=user, label=labels).save() for labels in label_list]
        except Exception as e:
            print(e)
            return JsonResponse({'code': -1, 'msg': '未获取到该用户'})

        return JsonResponse({'code': 200, 'msg': '完善信息成功！'})


def send_message(request):
    if request.method == 'GET':
        # 第一步 request.GET --> dict(key , value)  ['Name'] / get('Name')
        mobile = request.GET.get('mobile')
        print(mobile)
        # /user/send_message?mobile=
        if mobile is None or len(mobile) == 0:
            return JsonResponse({'code': -1, 'msg': '没有传递参数mobile'})
        tengxun = TengXun()
        code = Random_verify()
        results = tengxun.send_message(code, "18382776774")
        if results['result'] == 0:
            request.session.setdefault(mobile, code)
            request.session.set_expiry(600)
        else:
            return JsonResponse({'code': -2, 'msg': '发送失败'})
        return JsonResponse({'code': 200, 'msg': '发送成功！有效期10分钟'})


# 登录
def login(request):
    if request.method == 'POST':
        # user/login?mobile=1233344&pwd=dde   user/login?mobile=1233344&verify=235765
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        # 验证码
        verify = request.POST.get('verify')
        user = User.objects.filter(mobile=mobile).first()
        if not user:
            return JsonResponse({'code': -1, 'msg': '不存在该用户！'})
        if password is None:
            # 用验证码
            try:
                if verify == request.session[mobile]:
                    return JsonResponse({'code': 200, 'msg': '登录成功！'})
            except Exception as e:
                print(e)
                return JsonResponse({'code': -1, 'msg': '不存在该用户！'})
        else:
            if check_password(password, user.password):
                return JsonResponse({'code': 200, 'msg': '登录成功！'})
            else:
                return JsonResponse({'code': -1, 'msg': '手机号或密码错误！'})
        # 登录后 向session插入key:value   , key: user_id_手机号   value: user对象
        user_key = 'user_id_' + mobile
        request.session[user_key] = user
        return JsonResponse({'code': 200, 'msg': '请求成功！'})


def reset_password(request):
    if request.method == 'POST':
        pk = int(request.POST.get('user_id', 0))
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        verify = request.POST.get('verify')
        try:
            user = User.objects.get(pk=pk)
            if verify != request.session[mobile]:
                return JsonResponse({'code': -1, 'msg': '短信验证未通过'})
            user.password = make_password(password)
            user.save()
        except Exception as e:
            print(e)
            return JsonResponse({'code': -1, 'msg': '重置密码不成功'})
        return JsonResponse({'code': 200, 'msg': '重置密码成功！'})


# 我的
def index(request):
    if request.method == 'GET':
        mobile = request.GET.get('mobile', None)
        user_key = 'user_id_' + mobile
        user = request.session.get(user_key)
        username = user.username
        gender = user.gender
        dt = datetime.datetime.now()
        birthday = user.birthday
        age = dt.year - birthday.year
        phono = user.phono_set.filter(phono_type=1).first()
        phono_path = '' if phono is None else '/media/upload/' + phono.phono
        uuid_id = user.user_id
        # 获取关注、粉丝、互关数量
        ship_set = user.relationship_set
        gz_count = len(ship_set)
        fs_xount = Relationship.objects.filter(relation_id=user.id).count()
        hg_count = ship_set.filter(is_friends=True).count()
        # 朋友圈、标记点统计数量没做
        index = dict(mobile=mobile, id=id, username=username, gender=gender,
                     birthday=birthday, age=age, phono_path=phono_path, uuid_id=uuid_id,
                     gz_count=gz_count, fs_xount=fs_xount, hg_count=hg_count)
        return JsonResponse({'code': 200, 'msg': '', 'date': index})


# 修改用户信息
def update_user(request):
    if request.method == 'GET':
        pass
