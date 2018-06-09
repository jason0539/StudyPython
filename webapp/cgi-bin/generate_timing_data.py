#! /usr/local/bin/python3

import cgi
import cgitb
import athletemodel
import yate

cgitb.enable()
form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

print(yate.start_response())
print(yate.include_header("NUAC's Timing Data"))
print(yate.header("Athlete:"+athlete['Name']+",Dob:"+athlete['Dob']+"."))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete['top3']))
print(yate.para("The entire set of timing data is: " + str(athlete['data'])+".(dumplicates removed)"))

print(yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py","Add time":"test-form.py?AthleteId="+athlete_id}))