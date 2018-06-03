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
        file_content = data.strip().split(',')
        return (
            {
                'Name':file_content.pop(0),
                'Birthday':file_content.pop(0),
                'Grade':sorted(set([sanitize(each_time) for each_time in file_content]))
            }
        )
    except IOError as err:
        print('File error ' + str(err))
        return None

def printUserGrade(user):
    print(user['Name'] + "'s best grade is :" + str(user['Grade'][0:3]))

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
printUserGrade(james)
printUserGrade(julie)
printUserGrade(mikey)
printUserGrade(sarah)