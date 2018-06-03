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
sorted_james = sorted([sanitize(each_time) for each_time in james])
sorted_julie = sorted([sanitize(each_time) for each_time in julie])
sorted_mikey = sorted([sanitize(each_time) for each_time in mikey])
sorted_sarah = sorted([sanitize(each_time) for each_time in sarah])

uniqe_james = []
uniqe_julie = []
uniqe_mikey = []
uniqe_sarah = []

for each_time in sorted_james:
    if each_time not in uniqe_james:
        uniqe_james.append(each_time)

for each_time in sorted_julie:
    if each_time not in uniqe_julie:
        uniqe_julie.append(each_time)

for each_time in sorted_mikey:
    if each_time not in uniqe_mikey:
        uniqe_mikey.append(each_time)

for each_time in sorted_sarah:
    if each_time not in uniqe_sarah:
        uniqe_sarah.append(each_time)

print(uniqe_james)
print(uniqe_julie)
print(uniqe_mikey)
print(uniqe_sarah)

