import pickle
import os
import nester

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, role_spoken) = each_line.split(':',1)
            role_spoken = role_spoken.strip()
            if role == 'Man':
                man.append(role_spoken)
            elif role == 'Other Man':
                other.append(role_spoken)
        except ValueError:
            pass    
    data.close()
except IOError:
    print('The data file is missing!')

'''使用pickle存储'''
try:
    with open('man_data.txt','wb') as man_file, open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pickle error:'+str(pickle))

'''使用pickle读取'''
new_man_file = []

try:
    with open('man_data.txt','rb') as man_file:
        new_man_file = pickle.load(man_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pick error:' + str(err))

nester.print_lol(new_man_file)
# 检查第一行和最后一行与上面是否一致
print(new_man_file[0])
print(new_man_file[-1])