import os

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, role_spoken) = each_line.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            print(role_spoken,end='')        
        except ValueError:
            print('aha,there is an exception')
            pass    
    data.close()
except IOError:
    print('The data file is missing!')