from aip import AipImageCensor


#  图片识别
APP_ID = '16295532'
API_KEY = 'gWSlD06wqf8yADLNw1PSdIhI'
SECRET_KEY = 'pqxslzYtZvoDrpEN3qtebSexw8vqDlR7'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)


filePath = '../media/u0.jpg'


# 图片审核
def get_file_picture(filePath):
    with open(filePath, 'rb') as f:
        return f.read()


result = client.imageCensorUserDefined(get_file_picture(filePath))
print(result)


result1s = client.imageCensorUserDefined('http://www.example.com/image.jpg')
print(result1s)