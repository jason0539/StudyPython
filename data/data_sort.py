def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else :
        return time_string
    (mins,secs) = time_string.split(splitter)
    return mins + '.' + secs

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

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

print(uniqe_james[0:3])
print(uniqe_julie[0:3])
print(uniqe_mikey[0:3])
print(uniqe_sarah[0:3])

