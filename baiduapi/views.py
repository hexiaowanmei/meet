from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render
# import json
# import serial
# import time
# import csv
# from time import sleep
#
# def ajax_list(request):
#     data=[]
#     while True:
#         line = str(str(s.readline())[2:])
#         # print(line)
#         if line.startswith('$GNGGA'):
#             line=str(line).split(',')
#             # print("接收的数据："+ str(line))
#             # print("OK:"+str(line))
#             # print("指令名称: ", line[0])
#             # print("发送时间: ", line[1][:6])
#
#             # 经纬度转换
#             j = float(line[4][:-7])+float(line[4][-7:])/60
#             w = float(line[2][:-7])+float(line[2][-7:])/60
#
#             #时间
#             gpstime=time.strftime('%H:%M:%S',time.localtime(time.time()))
#
#             # id
#             global l
#             l= l + 1
#
#             # 添加数据
#             data.append(j)
#             data.append(w)
#             data.append(l)
#             data.append(gpstime)
#             print(data)
#             with open('./rec_gps.csv','a',newline='') as csvFile1:
#                 writer = csv.writer(csvFile1)
#                 writer.writerow((l,gpstime,j,w))
#                 csvFile.close()
#             return HttpResponse(json.dumps(data), content_type='application/json')
# s = serial.Serial('COM5', 115200)
# global l
# l = 0
# csvFile = open('./rec_gps.csv', 'a',encoding = 'utf-8',newline='')
# writer = csv.writer(csvFile)
# writer.writerow(('id','time','longitude','latitude'))

def test(request):
    if request.method == 'GET':
        return render(request, 'map.html')