import os

data = open('sketch.txt')

for each_line in data:
    #if (each_line.find(':') > 0):
    if not each_line.find(':') == -1:
        (role, role_spoken) = each_line.split(':',1)
        print(role,end='')
        print(' said: ',end='')
        print(role_spoken,end='')
    
data.close()