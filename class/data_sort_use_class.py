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

class Athlete:
    def __init__(self,name,birthday=None,grade=[]):
        self.name = name
        self.birthday = birthday
        self.grade = grade
    
    def top3(self):
        return (sorted(set([sanitize(each_time) for each_time in self.grade]))[0:3])

    def add_time(self,time_value):
        self.grade.append(time_value)
    
    def add_times(self,list_of_times):
        self.grade.extend(list_of_times)

'''从文件读取时间item'''
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        file_content = data.strip().split(',')
        return (Athlete(file_content.pop(0),file_content.pop(0),file_content))
    except IOError as err:
        print('File error ' + str(err))
        return None

def printUserGrade(user):
    print(user.name + "'s best grade is :" + str(user.top3()))

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
printUserGrade(james)
printUserGrade(julie)
printUserGrade(mikey)
printUserGrade(sarah)