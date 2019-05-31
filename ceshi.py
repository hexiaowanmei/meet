# from urllib import parse
# import hashlib
#
#
# def get_urt(address):
#     # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=你的ak
#     queryStr = '/geocoder/v2/?address=%s&output=json&ak=5v679ZKDIgDOmpqfqSs3OQZkvVE9MzPX' % address
#
#     # 对queryStr进行转码，safe内的保留字符不转换
#     encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
#
#     # 在最后直接追加上yoursk
#     rawStr = encodedStr + '你的sk'
#
#     # 计算sn
#     sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())
#
#     # 由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
#     url = parse.quote("http://api.map.baidu.com" + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
#
#     return url
#
# print(get_urt('成都市保利中心'))
# import turtle
# import time
#
#
# # 画心形圆弧
# def hart_arc():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(2)
#
#
# def move_pen_position(x, y):
#     turtle.hideturtle()  # 隐藏画笔（先）
#     turtle.up()  # 提笔
#     turtle.goto(x, y)  # 移动画笔到指定起始坐标（窗口中心为0,0）
#     turtle.down()  # 下笔
#     turtle.showturtle()  # 显示画笔
#
#
# # love = input("请输入表白话语，默认为‘I Love You’：")
# love = 'I Love You'
# # signature = input("请签署你的大名，不填写默认不显示：")
# signature = '何萧'
#
#
# if love == '':
#     love = 'I Love You'
#
# # 初始化
# turtle.setup(width=800, height=500)  # 窗口（画布）大小
# turtle.color('red', 'pink')  # 画笔颜色
# turtle.pensize(3)  # 画笔粗细
# turtle.speed(1)  # 描绘速度
# # 初始化画笔起始坐标
# move_pen_position(x=0, y=-180)  # 移动画笔位置
# turtle.left(140)  # 向左旋转140度
#
# turtle.begin_fill()  # 标记背景填充位置
#
# # 画心形直线（ 左下方 ）
# turtle.forward(224)  # 向前移动画笔，长度为224
# # 画爱心圆弧
# hart_arc()  # 左侧圆弧
# turtle.left(120)  # 调整画笔角度
# hart_arc()  # 右侧圆弧
# # 画心形直线（ 右下方 ）
# turtle.forward(224)
#
# turtle.end_fill()  # 标记背景填充结束位置
#
# # 在心形中写上表白话语
# move_pen_position(0, 0)  # 表白语位置
# turtle.hideturtle()  # 隐藏画笔
# turtle.color('#CD5C5C', 'pink')  # 字体颜色
# # font:设定字体、尺寸（电脑下存在的字体都可设置）  align:中心对齐
# turtle.write(love, font=('Arial', 30, 'bold'), align="center")
#
# # 签写署名
# if signature != '':
#     turtle.color('red', 'pink')
#     time.sleep(2)
#     move_pen_position(180, -180)
#     turtle.hideturtle()  # 隐藏画笔
#     turtle.write(signature, font=('Arial', 20), align="center")
#
# # 点击窗口关闭程序
# window = turtle.Screen()
# window.exitonclick()