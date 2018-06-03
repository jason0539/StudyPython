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

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

'''逐个转换'''
# clean_james = []
# clean_julie = []
# clean_mikey = []
# clean_sarah = []

# for each_time in james:
#     clean_james.append(sanitize(each_time))
# for each_time in julie:
#     clean_julie.append(sanitize(each_time))
# for each_time in mikey:
#     clean_mikey.append(sanitize(each_time))
# for each_time in sarah:
#     clean_sarah.append(sanitize(each_time))

'''列表推导转换
mins = [1,2,3]
secs = [m * 60 for m in mins]

meters = [1,10,3]
feet = [m * 3.281 for m in meters]
'''
uniqe_james = sorted(set([sanitize(each_time) for each_time in james]))
uniqe_julie = sorted(set([sanitize(each_time) for each_time in julie]))
uniqe_mikey = sorted(set([sanitize(each_time) for each_time in mikey]))
uniqe_sarah = sorted(set([sanitize(each_time) for each_time in sarah]))

'''循环去重demo'''
# for each_time in sorted_james:
#     if each_time not in uniqe_james:
#         uniqe_james.append(each_time)

print(uniqe_james[0:3])
print(uniqe_julie[0:3])
print(uniqe_mikey[0:3])
print(uniqe_sarah[0:3])

