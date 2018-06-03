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

class AthleteList(list):
    def __init__(self,name,birthday=None,grade=[]):
        list.__init__([])
        self.name = name
        self.birthday = birthday
        self.extend(grade)
    
    def top3(self):
        return (sorted(set([sanitize(each_time) for each_time in self]))[0:3])


'''从文件读取时间item'''
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        file_content = data.strip().split(',')
        return (AthleteList(file_content.pop(0),file_content.pop(0),file_content))
    except IOError as err:
        print('File error ' + str(err))
        return None

def printUserGrade(user):
    print(user.name + "'s best grade is :" + str(user.top3()))

james = get_coach_data('james.txt')
james.append('0.01')
julie = get_coach_data('julie.txt')
julie.extend(['0.01','0.02','0.03'])
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
printUserGrade(james)
printUserGrade(julie)
printUserGrade(mikey)
printUserGrade(sarah)