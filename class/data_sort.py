'''统一时间item中的特殊字符'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else :
        return time_string
    (mins,secs) = time_string.split(splitter)
    return mins + '.' + secs

'''从文件读取时间item'''
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as err:
        print('File error ' + str(err))
        return None

sarah = get_coach_data('sarah.txt')

# 继续使用列表存储数据结构
(name,birthday) = sarah.pop(0),sarah.pop(0)
grade = sorted(set([sanitize(each_time) for each_time in sarah]))[0:3]
print(name + "'s best grade is :" + str(grade))

