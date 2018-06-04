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
