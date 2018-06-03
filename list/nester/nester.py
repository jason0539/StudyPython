''' 安装该模块到本地
    1.python3 setup.py sdist
    2.python3 setup.py install
'''
import sys

def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=fn)
            print(each_item,file=fn)