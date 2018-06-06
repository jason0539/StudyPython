#! /usr/local/bin/python3

import cgi
import cgitb
import athletemodel
import yate

cgitb.enable()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
athleteList = athletemodel.get_from_store()

athlete = athleteList[athlete_name]

print(yate.start_response())
print(yate.include_header("Coach Kelley's Timing Data"))
print(yate.header("Athlete:"+athlete.name+",birthday:"+athlete.dob+"."))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete.top3))

print(yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py"}))