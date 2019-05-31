import json
import re

from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from homepage.models import *
from user.models import User, Phono
from django.http import JsonResponse
from homepage.test01 import *
from django.core import serializers

'遇见主页'


def homepage(request):
    if request.method == 'GET':
        data = {}
        result_list = []
        # user_id = request.session.get('user_id')
        user_id = request.GET.get('user_id')
        user = User.objects.filter(id=user_id).first()
        user_count = Count.objects.filter(user_id=user_id).first()
        sum_count = user_count.count
        friend_lists = user.meetnum_set.order_by('-id')
        # data_result = serializers.serialize('json', friend_list)
        # data_result = json.loads(data_result)
        # data['sum_count'] = sum_count
        # data['user_friend'] = data_result
        for friend_list in friend_lists:
            user_friend_id = friend_list.meetcount
            user_friend = User.objects.filter(id=user_friend_id).first()
            # friend_photo = Phono.objects.filter(user_id=user_friend_id).frist()
            meet_count = user.meetnum_set.filter(meetcount=user_friend_id).all().count()
            result_dict = {}
            # result_dict['gender'] = friend_list.gender
            result_dict['age'] = friend_list.age
            result_dict['distance'] = friend_list.distance
            # result_dict['username'] = user_friend.username
            result_dict['meettime'] = friend_list.meettime
            # result_dict['friend_photo'] = friend_photo.phono
            result_dict['meet_count'] = meet_count
            result_list.append(result_dict)
        sum_count = Count.objects.filter(user_id=user_id).first()
        sum_count = sum_count.count
        data['sum_count'] = sum_count
        data['result'] = result_list

        return JsonResponse({'code': 200, 'msg': '请求成功', 'data': data})


def user_friend(request):
    '遇见人的列表'
    if request.method == 'POST':
        condition = request.POST['condition']
        lng = request.POST['lng']
        lat = request.POST['lat']
        gender = request.POST['gender']
        min_age = request.POST['min_age']
        max_age = request.POST['max_age']
        user_id = request.POST.get('user_id')
        # user_id = request.session.get('user_id')
        user = User.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse({'code': 203, 'msg': '请先登录'})
        else:
            User.objects.filter(id=user_id).update(longitude=lng, latitude=lat)
            user_address = locatebyLatLng(lat, lng)
            user_add = geoadd(lng, lat, user_address)
            user_msgs = georadiusbymember(user_address, condition)
            for user_msg in user_msgs:
                user_site = user_msg[0].decode()
                user_distance = user_msg[1]
                coordinate = geopos(user_site)
                x = float(str(coordinate[0][0])[:10])
                # x = coordinate[0][0]
                y = float(str(coordinate[0][1])[:9])
                user_other = User.objects.filter(Q(longitude=x) & Q(latitude=y)).first()

                # meet_num = MeetNum.objects.filter(user_id=user_other.id).all.count()
                # if meet_num <= 2:
                #     MeetNum.objects.create(user_id=user_other.id, distance=user_distance, age=user_other.age,
                #                            gender=user_other.gender, nums=3, site=user_address)
                #     MeetSite.objects.create(user_id=user_other.id, site=user_address, longitude=x, latitude=y)
                # elif meet_num <= 2:
                #     MeetNum.objects.create(user_id=user_other.id, distance=user_distance, age=user_other.age,
                #                            gender=user_other.gender, nums=3, site=user_address)
                #     MeetSite.objects.create(user_id=user_other.id, site=user_address, longitude=x, latitude=y)
                #
                # meet_count = MeetNum.objects.all().count()
                # if not meet_count:
                #     return JsonResponse({'code': 200, 'msg': '附近没人'})
                # else:
                #     meet_count += meet_count
                #     Count.objects.create(user_id=user.id, count=meet_count)
                #

                if user_other == None or user.id == user_other.id:
                    continue
                else:
                    '遇见总人数'

                    if gender == user_other.gender and user_other.age in range(min_age, max_age):
                        meet_friend = user.meetnum_set.filter(meetcount=user_other.id).all().count()
                        meet_count = Count.objects.filter(user_id=user_id).first()
                        count = meet_count.count
                        if count and meet_friend < 2:
                            count += 1
                            # meetcount = MeetNum.objects.filter(user_id=user_other.id).all().count()

                            # if meetcount < 2:
                            user.meetnum_set.create(distance=user_distance, site=user_address,
                                                    age=user_other.age, meetcount=user_other.id, longitude=x,
                                                    latitude=y)
                            Count.objects.filter(user_id=user_id).update(count=count)
                        elif meet_friend >= 2:
                            continue
                        else:
                            user.meetnum_set.create(distance=user_distance, site=user_address,
                                                    age=user_other.age, meetcount=user_other.id, longitude=x,
                                                    latitude=y)
                            Count.objects.create(user_id=user_id, count=1)

                    else:
                        continue
                    # if count and meet_friend < 2:
                    #     count += 1
                    #     # meetcount = MeetNum.objects.filter(user_id=user_other.id).all().count()
                    #
                    #     # if meetcount < 2:
                    #     user.meetnum_set.create(distance=user_distance, site=user_address,
                    #                             age=user_other.age, meetcount=user_other.id, longitude=x, latitude=y)
                    #     Count.objects.filter(user_id=user_id).update(count=count)
                    # elif meet_friend >= 2:
                    #     continue
                    # else:meet_count
                    #     user.meetnum_set.create(distance=user_distance, site=user_address,
                    #                             age=user_other.age, meetcount=user_other.id, longitude=x, latitude=y)
                    #     Count.objects.create(user_id=user_id, count=1)
            else:
                JsonResponse({'code': 201, 'msg': '附近没人'})

        return JsonResponse({'code': 200, 'msg': '请求成功'})


'遇见次数'


def meet_count(request):
    if request.method == 'GET':
        user_friend_id = request.GET['user_id']
        # user_id = request.session['user_id']
        user = User.objects.filter(id=1).first()
        if not user:
            return JsonResponse({'code': 203, 'msg': '请先登录'})
        else:
            meet_count = user.meetnum_set.filter(meetcount=user_friend_id).all().count()
            return JsonResponse({'code': 200, 'msg': '请求成功', 'data': meet_count})

        #     user_id = User.objects.filter(id=user_friend_id).first()
        #     meet_user_id = MeetNum.objects.filter(user_id=user_id.id).first()
        #     meet_user = MeetSite.objects.filter(user_id=user_id.id).first()
        #     '记录相遇点'
        #     meet_site = meet_user_id.site
        #     '和同一个人相遇的次数'
        #     if meet_user:
        #         nums = MeetSite.objects.filter(user_id=user_id.id).last()
        #         count = nums.nums
        #         count += 1
        #
        #         meet_site_count = MeetSite.objects.all().count()
        #         '相遇点达到5次，就删除一次再进行增加'
        #         if meet_site_count >= 5:
        #             meet_site_list = MeetSite.objects.all()
        #             user_num = meet_site_list[0].id
        #             MeetSite.objects.filter(id=user_num).delete()
        #             MeetSite.objects.create(user_id=user_id.id, site=meet_site, nums=count)
        #         else:
        #             MeetSite.objects.create(user_id=user_id.id, nums=count, site=meet_site)
        #     else:
        #         '没有和这个人相遇'
        #         MeetSite.objects.create(user_id=user_id.id, nums=1, site=meet_site)
        #     meet_nums = MeetSite.objects.order_by('-id')
        #     data = {}
        #     data_site = []
        #     for meet_num in meet_nums:
        #         data_site.append(meet_num.site)
        #     data['site'] = data_site
        # return JsonResponse({'code': 200, 'msg': '请求成功', 'data': data})


'右滑左滑'


def slide(request):
    '我喜欢的人'
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        liketype = request.POST['liketype']
        # user = request.session['user_id']
        user = 1
        u = User.objects.get(id=user)
        user = User.objects.filter(id=user_id).first()
        count = MeetSite.objects.filter(user_id=user_id).first()
        count.nums += 1
        if liketype == '1':
            '右滑喜欢'
            count = u.meetlike_set.all().count()
            if count <= 52:
                name = User.objects.filter(id=user_id).first()
                user.meetlike_set.create(username=name.username)
            else:
                return JsonResponse({'code': 202, 'msg': '喜欢人已满'})
        if liketype == '0':
            '左滑不喜欢'
            u.meetunlike_set.create(username=user.username, count=count.nums)
        MeetSite.objects.filter(user_id=user_id).update(nums=count.nums)
        meet_num = MeetSite.objects.filter(user_id=user_id).first()
        data = meet_num.nums
        return JsonResponse({'code': 200, 'msg': '请求成功'})


'返回上一个不喜欢的用户'


def last_user(requset):
    if requset.method == 'GET':
        # user_id = requset.session['user_id']
        user_id = requset.GET['user_id']
        user = User.objects.get(id=user_id)
        lastuser = user.meetunlike_set.order_by('-id')
        if lastuser:
            x = lastuser[0]
            unuser = User.objects.filter(username=x.username).values()
            data = unuser[0]
            return JsonResponse({'code': 200, 'msg': '请求成功', 'data': data})
        else:
            return JsonResponse({'code': 203, 'msg': '先去遇见人吧'})


'筛选'


def screen(request):
    if request.method == 'POST':
        '性别年龄距离'
        gender = request.POST['gender']
        min_age = request.POST['min_age']
        max_age = request.POST['max_age']
        max_distance = request.POST['max_distance']
        # user_id = request.session['user_id']
        user_id = request.POST['user_id']
        user = User.objects.filter(id=user_id).first()
        data = {}
        result_list = []
        if gender == '男':
            girl_users = user.meetnum_set.filter(
                Q(distance__lte=(max_distance)) & Q(gender='女') & Q(age__range=(min_age, max_age))).order_by('-id')
            for girl_user in girl_users:
                result = {}
                user = girl_user.user.first()
                result['id'] = user.id
                result['username'] = user.username
                result['age'] = user.age
                result['gender'] = user.gender
                result['distance'] = girl_user.distance
                result['site'] = girl_user.site
                result['meettime'] = girl_user.meettime
                result_list.append(result)
                data['user'] = result_list

        elif gender == '女':
            boy_users = user.meetnum_set.filter(
                Q(distance__lte=(max_distance)) & Q(gender='男') & Q(age__range=(min_age, max_age))).all().order_by(
                '-id')
            for boy_user in boy_users:
                result = {}
                user = boy_user.user.first()
                result['id'] = user.id
                result['username'] = user.username
                result['age'] = user.age
                result['gender'] = user.gender
                result['distance'] = boy_user.distance
                result['site'] = boy_user.site
                result['meettime'] = boy_user.meettime
                result_list.append(result)
                data['user'] = result_list
        else:
            all_users = user.meetnum_set.filter(
                Q(distance__lte=(max_distance)) & Q(age__range=(min_age, max_age))).order_by('-id')
            for all_user in all_users:
                user = all_user.user.first()
                result = {}
                result['id'] = user.id
                result['username'] = user.username
                result['age'] = user.age
                result['gender'] = user.gender
                result['distance'] = all_user.distance
                result['site'] = all_user.site
                result['meettime'] = all_user.meettime
                result_list.append(result)
                data['user'] = result_list
        return JsonResponse({'code': 200, 'msg': '请求成功', 'data': data})


'相遇点'


def meets_site(request):
    if request.method == 'GET':
        user_friend_id = request.GET['user_id']
        # user_id = request.session.get('user_id')
        user = User.objects.filter(id=1).first()
        user_friend = User.objects.filter(id=user_friend_id).first()
        if not user:
            return JsonResponse({'code': 203, 'msg': '请先登录'})
        else:
            # user_id = User.objects.filter(id=user_id).first()
            meet_user_id = user.meetnum_set.filter(meetcount=user_friend_id).all()
            # result = []
            data = {}
            for meet_friend in meet_user_id:
                user_dict = {}
                user_friend_dict = {}
                lng = meet_friend.longitude
                lat = meet_friend.latitude
                meet_sites = meet_friend.site
                meet_coord = geopos(meet_sites)
                user_lng = str(meet_coord[0][0])[:10]
                user_lat = str(meet_coord[0][1])[:9]
                user_dict['user_lng'] = user_lng
                user_dict['user_lat'] = user_lat
                # user_dict['user_photo'] = user.photo
                user_friend_dict['lng'] = lng
                user_friend_dict['lat'] = lat
                # user_friend_dict['user_friend_photo'] = user_friend.photo
                data['user'] = user_dict
                data['user_friend'] = user_friend_dict
            return JsonResponse({'code': 200, 'msg': '请求成功', 'data': data})
