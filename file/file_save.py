import os

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

try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')

    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('File error.')
finally:
    man_file.close()
    other_file.close()