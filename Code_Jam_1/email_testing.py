import smtplib
import json

with open('Blood_grp_A_neg.json') as json_file:
     data = json.load(json_file)

server = smtplib.SMTP("smtp.cc.iitk.ac.in",25)
server.starttls()
server.login('amiteshs', 'amitesh163a@')

msg = 'Subject: Need Blood in Emergency : Blood Donations\n\nHello Students,\nA friend of yours, Mukesh, in is need of blood urgently of' + params[0] + 'blood group. Please do come and donate blood for him.\nKindly extend help.'

for i in len(data):
	server.sendmail('amiteshs@iitk.ac.in', 'amiteshs@iitk.ac.in', msg)

server.quit()
