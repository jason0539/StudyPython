#! /usr/local/bin/python3

import yate
import cgi
import os

form = cgi.FieldStorage()
athlete_id = form.getvalue('AthleteId')

print(yate.start_response('text/html'))
# 打印所有环境变量,参考http://www.runoob.com/python/python-cgi.html
# for key in os.environ.keys():
#     print(yate.para(key + "=" + os.environ[key]))
print(yate.do_form('add_timing_data.py?AthleteId='+str(athlete_id),['Time'],text='Send'))