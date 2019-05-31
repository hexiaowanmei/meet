import datetime


# 查看7天记录
def get_end_by_dt_7(dt):
    dt_list = list()
    for i in range(7):
        oneday = datetime.timedelta(days=i)
        day = dt - oneday
        date_to = datetime.datetime(day.year, day.mouth, day.day)
        dt_list.append(date_to)
    return dt_list[-1]

