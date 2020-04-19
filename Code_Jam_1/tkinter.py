from Tkinter import *
import Tkinter as tk
import tkMessageBox
import json
import smtplib

global data_A_neg
global data_B_neg
global data_AB_neg
global data_O_neg
global data_A_pos
global data_B_pos
global data_AB_pos
global data_O_pos

def Open_files_1():
	global data_A_neg
	with open('Blood_grp_A_neg.json') as json_file:
    		data_A_neg = json.load(json_file)
def Open_files_2():
	global data_B_neg
	with open('Blood_grp_B_neg.json') as json_file:
			data_B_neg = json.load(json_file)
def Open_files_3():
    global data_AB_neg
    with open('Blood_grp_AB_neg.json') as json_file:
    		data_AB_neg = json.load(json_file)
def Open_files_4():
	global data_O_neg
	with open('Blood_grp_O_neg.json') as json_file:
			data_O_neg = json.load(json_file)
def Open_files_5():
	global data_A_pos
	with open('Blood_grp_A_pos.json') as json_file:
			data_A_pos = json.load(json_file)
def Open_files_6():
	global data_B_pos
	with open('Blood_grp_B_pos.json') as json_file:
			data_B_pos = json.load(json_file)
def Open_files_7():
	global data_AB_pos
	with open('Blood_grp_AB_pos.json') as json_file:
			data_AB_pos = json.load(json_file)
def Open_files_8():
	global data_0_pos
	with open('Blood_grp_O_pos.json') as json_file:
			data_O_pos = json.load(json_file)
    
def SendMails():
	
	Open_files_1()
	Open_files_2()
	Open_files_3()
	Open_files_4()
	Open_files_5()
	Open_files_6()
	Open_files_7()
	Open_files_8()
	
	server = smtplib.SMTP("smtp.cc.iitk.ac.in",25)
	server.starttls()
	server.login('amiteshs', 'amitesh163a@')

	msg = 'Subject: Need Blood in Emergency : Blood Donations\n\nHello Students,\n\nA friend of yours, ' + params[1] + ', in is need of blood urgently of ' + params[0] + ' blood group. Please do come and donate blood for him.\n\nKindly extend help.\n\n' + params[2] +'\nHealth center\nIITK'

	if(params[0]=='A-'):
		for i in range(len(data_A_neg)):
			server.sendmail(params[3], data_A_neg[i], msg)
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
	elif(params[0]=='B-'):
		for i in range(len(data_B_neg)):
			server.sendmail(params[3], data_B_neg[i], msg)
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
	elif(params[0]=='AB-'):
		for i in range(len(data_AB_neg)):
			server.sendmail(params[3], data_AB_neg[i], msg)
		for i in range(len(data_A_neg)):
			server.sendmail(params[3], data_A_neg[i], msg)
		for i in range(len(data_B_neg)):
			server.sendmail(params[3], data_B_neg[i], msg)
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
	elif(params[0]=='O-'):
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
	elif(params[0]=='A+'):
		for i in range(len(data_A_neg)):
			server.sendmail(params[3], data_A_neg[i], msg)
		for i in range(len(data_A_pos)):
			server.sendmail(params[3], data_A_pos[i], msg)
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
		for i in range(len(data_O_pos)):
			server.sendmail(params[3], data_O_pos[i], msg)
	elif(params=='B+'):
		for i in range(len(data_B_neg)):
			server.sendmail(params[3], data_B_neg[i], msg)
		for i in range(len(data_B_pos)):
			server.sendmail(params[3], data_B_pos[i], msg)
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
		for i in range(len(data_O_pos)):
			server.sendmail(params[3], data_O_pos[i], msg)
	elif(params[0]=='AB+'):
		for i in range(len(data_A_neg)):
			server.sendmail(params[3], data_A_neg[i], msg)
		for i in range(len(data_A_pos)):
			server.sendmail(params[3], data_A_pos[i], msg)
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
		for i in range(len(data_O_pos)):
			server.sendmail(params[3], data_O_pos[i], msg)
		for i in range(len(data_B_neg)):
			server.sendmail(params[3], data_B_neg[i], msg)
		for i in range(len(data_B_pos)):
			server.sendmail(params[3], data_B_pos[i], msg)
		for i in range(len(data_AB_neg)):
			server.sendmail(params[3], data_A_neg[i], msg)
		for i in range(len(data_AB_pos)):
			server.sendmail(params[3], data_A_pos[i], msg)
	elif(params[0]=='O+'):
		for i in range(len(data_O_neg)):
			server.sendmail(params[3], data_O_neg[i], msg)
		for i in range(len(data_O_pos)):
			server.sendmail(params[3], data_O_pos[i], msg)
	print(data_A_neg[0])			
	server.quit()
    
    
top = tk.Tk()
top.title("Mailing System for Blood Requirement")
top.geometry('400x300')


def helloCallBack():
    tkMessageBox.showinfo("info","Choose the Blood Group of the patient for blood requirement")

B= tk.Button(top, text ="Information",font=(12), command = helloCallBack, bd = 2, relief=RAISED, width=30)
B.pack()

L1 = Label(top, text="Enter the reqiured Blood Group", font = 14)
L1.pack()

Blood_grp = Entry(top)
Blood_grp.pack()

L2 = Label(top, text='Enter the Name of the person who requires blood', font = 14)
L2.pack()

Name_person = Entry(top)
Name_person.pack()

L2 = Label(top, text='Enter the name of the sender', font = 14)
L2.pack()

Sender_person = Entry(top)
Sender_person.pack()

L2 = Label(top, text='Enter the email address of the sender', font = 14)
L2.pack()

email = Entry(top)
email.pack()

def getInput():

    a = Blood_grp.get()
    b = Name_person.get()
    c = Sender_person.get()
    d = email.get()

    global params
    params = [a,b,c,d]
    
    popup = tk.Tk()
    popup.title("Confirm the Details")
    popup.geometry('200x200')
    label1 = Label(popup, text = params[0], font='14')
    label1.pack()
    label2 = Label(popup, text = params[1], font='14')
    label2.pack()
    label3 = Label(popup, text = params[2], font='14')
    label3.pack()
    label4 = Label(popup, text = params[3], font='14')
    label4.pack()
    B = Button(popup, text="Confirm", command = popup.destroy)
    B.pack()
    popup.mainloop()

L5 = Label(top, text='First Click the Submit Button for saving\nfilled in details', font = '14')
L5.pack()

B1 = Button(top, text = "Submit", command = getInput, relief=RAISED)
B1.pack()

B2 = Button(top, text='Send Mail', command = SendMails, relief=RAISED)
B2.pack()

top.mainloop()
