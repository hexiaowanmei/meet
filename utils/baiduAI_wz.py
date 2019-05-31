from aip import AipOcr

# 定义常量
APP_ID = '16295390'
API_KEY = 'ufOyfhSxGHX1yZPNKGT0XoS8'
SECRET_KEY = 'NqvZz1md33Wx6BLoaG7Ga6X45Tgz2HcW'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)


filePath = "../media/aa.jpg"


# 文字审核
def get_file_content(filePath):
    with open(filePath, 'rb') as f:
        return f.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)
