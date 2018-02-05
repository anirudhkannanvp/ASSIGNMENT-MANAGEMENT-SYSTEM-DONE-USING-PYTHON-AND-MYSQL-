import MySQLdb
import webbrowser
import os
import getpass

username=""

sp1="\t\t\t\t\t\t\t"
sp2="\t\t\t\t\t\t"
en1="\n\n\n\n\n\n\n\n\n\n"
en2="\n\n"

adminpass="12345678"

def delay():
	d=0;
	while(d<10000000):	
			d+=1

def createpassword():
	global password
	password=getpass.getpass(prompt=en2+sp1+"  Enter Password: ")
	global cpassword
	cpassword=getpass.getpass(prompt=en2+sp1+"Confirm Password: ")
	if(cpassword==password):
		return 1
	else:
		return 0

numlines=0

def copycase(roll1,roll2,ass1):
	s1="GIVE FILE 1 NAME HERE"
	s2="GIVE FILE 2 NAME HERE"

	try:
		f1=open(s1,'r')
		f2=open(s2,'r')
	except:
		print en2+sp2+"NOT AVAILABLE"
	with open(s1,'r') as file1:
		with open(s2, 'r') as file2:
			same = set(file2).intersection(file1)
	
	same.discard("\n")
	lin=0

	with open('COPY CASE FILE.TXT', 'w') as file_out:
		iniscore=100
		for line in same:
			iniscore-=1
			lin=lin+1
			file_out.write(line)
		file_out.write("\n\n\n")
		file_out.write("THE COPY CASE HAS BEEN IDENTIFIED AND NO OF COPIED LINES IS :")
		file_out.write(str(lin))
		percent1=(100-lin)
		file_out.write("\n\n\n")
		file_out.write("FINAL SCORE IS :")
		file_out.write(str(iniscore))
		file_out.write("\n\n\n")
	webbrowser.open('/home/anirudh/itwsfiles/copycases/s1c.txt')
	delay()

def copy():
	os.system('clear')
	print en1+sp2+"      COPY CASE DETECTOR"
	print     sp2+"      ------------------"
	p=data.cursor()
	p.execute("SELECT ROLLNO,NAME FROM sbase ")
	n=p.fetchall()
	for i in n:
		print en2+sp2+"       "+str(i[0])+"--"+str(i[1])
	print en2+sp2+"  ENTER FIRST ROLL NO :",
	a=raw_input()
	print en2+sp2+"  ENTER SECOND ROLL NO :",
	b=raw_input()
	print en2+sp2+"    ENTER ASSIGNMENT :",
	c=raw_input()
	copycase(a,b,c)
	delay()



def createstudent():
	os.system('clear')	
	print en1+sp1+"        Welcome!"
	print en2+sp1+"Enter Username: ",
	global username
	username=raw_input()
	global roll
	print en2+sp2+"     Enter Roll Number: ",
	roll=raw_input()
	temp=createpassword()
	while (temp!=1):
		print "Passwords do not match.Please enter matching passwords"
		temp=createpassword()
	p=data.cursor()
	p.execute("INSERT INTO sbase(ROLLNO,NAME,PASSWORD) VALUES(%s,%s,%s)",(roll,username,password))
	os.makedirs("/home/anirudh/itwsfiles/submissions/"+str(roll))
	data.commit()
	delay()

def subass(n):
	os.system('clear')
	p=data.cursor()	
	ch=assignmentselectadmin(p)
	while(True):	
		os.system('clear')
		print en1+sp1+"   LOGGED IN AS ",
		print n
		print en2+sp2+"  ENTER PATH: ",
		p.execute("SELECT ROLLNO FROM sbase WHERE NAME = %s",(n,))	
		x=raw_input()		
		roll=p.fetchall()	
		y="/home/anirudh/itwsfiles/submissions/"+str(roll[0][0])+"/assign"+str(ch)+".txt"
		try:	
			f1=open(x,"r")
			break
		except:
			print "SORRY FILE NOT FOUND"	
	f2=open("/home/anirudh/itwsfiles/submissions/"+str(roll[0][0])+"/assign"+str(ch)+".txt","w")
	s1=f1.read()
	f2.write(s1)
	com="UPDATE sbase SET ASSIGN"+str(ch)+" = 'SUBMITTED' WHERE NAME = '"+n+"'"
	p.execute(com)
	data.commit()
	f1.close()
	f2.close()
	print en2+sp1+"   ASSIGNMENT SUBMITTED"
	delay()
	

def viewmarks(n):
	os.system('clear')
	print en1+sp1+"   LOGGED IN AS ",
	print n
	p=data.cursor()
	ch=int(assignmentselectadmin(p))
	dat=p.execute("SELECT * FROM sbase WHERE NAME = %s",(n,))
	quer=p.fetchall()
	if(quer[0][3+(ch-1)*3]=="PENDING"):
		print en2+sp1+"     ASSIGNMENT PENDING "
	elif(quer[0][5+(ch-1)*3]==0):
		print en2+sp1+"     EVALUATION PENDING "
	else:
		print en2+sp1+"      MARKS OBTAINED:",
		print quer[0][5+(ch-1)*3]
	delay()



def messageselectstud(p):
	os.system('clear')
	print en1+sp1+"      SELECT MESSAGE "
	print     sp1+"      -----------------"
	nofile=len(os.listdir("/home/anirudh/itwsfiles/messages"))
	for i in range(nofile):
		print en2+sp1+"          MESSAGE ",i+1,"\n"
	print en2+sp1+"      SELECT CHOICE: ",
	ch=int(raw_input())
	return ch;


def readmess():
	p=data.cursor()
	ch=messageselectstud(p)
	fn="/home/anirudh/itwsfiles/messages/"+"/message"+str(ch)+".txt"
	webbrowser.open(fn)
	delay()
	

def acceptstud():
	os.system('clear')
	print en1+sp1+" ENTER ROLLNO",
	y=raw_input()
	p=data.cursor()
	p.execute("SELECT PASSWORD FROM sbase WHERE ROLLNO = %s ",(y,))	
	q=p.fetchall()
	z=q[0][0]	
	x=getpass.getpass(prompt=en2+sp1+"  Enter Password: ")
	while(x!=z):
		print en2+sp1+"     WRONG PASSWORD"
		d=0
		delay()
		os.system('clear')
		print en1+sp1+" ENTER ROLLNO",
		y=raw_input()
		x=getpass.getpass(prompt=en2+sp1+"  Enter Password: ")
		p=data.cursor()
		p.execute("SELECT PASSWORD FROM sbase WHERE ROLLNO = %s ",(y,))	
		q=p.fetchall()
		z=q[0][0]		
	p.execute("SELECT NAME FROM sbase WHERE ROLLNO = %s ",(y,))
	na=p.fetchall()
	print na[0][0]
	username=na[0][0]
	os.system('clear')
	return username

def printstudmenu(n):
	os.system('clear')
	print en1+sp1+"   LOGGED IN AS ",
	print n
	print sp1+    "---------------------------"
	print en2+sp1+"   1.SUBMIT ASSIGNMENT"
	print en2+sp1+"     2.READ MESSAGES"
	print en2+sp1+"     3.CHECK STATUS"
	print en2+sp1+"        4.LOG OUT"
	print en2+sp1+"    ENTER CHOICE:",
	x=int(raw_input())
	return x

def acceptad():
	os.system('clear')
	x=""
	x=getpass.getpass(prompt=en1+sp1+"  Enter Password: ")
	while(x!=adminpass):
		print en2+sp1+"     WRONG PASSWORD"
		d=0
		delay()
		os.system('clear')
		x=getpass.getpass(prompt=en1+sp1+"  Enter Password: ")
	os.system('clear')

def printadminmenu():
	os.system('clear')
	print en1+sp1+" LOGGED IN AS ADMINISTRATOR"
	print sp1+    "---------------------------"
	print en2+sp1+"   1. VIEW SUBMISSIONS"
	print en2+sp1+"      2.SEND MESSAGE"
	print en2+sp1+"     3.ADD ASSIGNMENT"
	print en2+sp1+"     4.ALTER DEADLINE"
	print en2+sp1+"    5.CHECK COPY CASES"
	print en2+sp1+"        6.LOG OUT"
	print en2+sp1+"       ENTER CHOICE:",
	x=int(raw_input())
	return x

def assignmentselectadmin(p):
	os.system('clear')
	print en1+sp1+"      SELECT ASSIGNMENT "
	print     sp1+"      -----------------"
	p.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema='itws' AND table_name='sbase'")
	z=p.fetchall()
	noas=(z[0][0]/3)-1
	for i in range(noas):
		print en2+sp1+"       ASSIGNMENT ",i+1,"\n"
	delay()
	print en2+sp1+"      SELECT CHOICE: ",
	ch=int(raw_input())
	return ch;

def sendmess():
	os.system('clear')
	print en1+sp1+"       SEND MESSAGE "
	print en2+sp2+"	  ENTER MESSAGE: ",
	mes=raw_input()
	mes=mes+'\n'
	nofile=len(os.listdir("/home/anirudh/itwsfiles/messages"))
	nofile=nofile+1
	s="/home/anirudh/itwsfiles/messages/message"+str(nofile)+".txt"
	try:
		f=open(s,"w")
		f.write(mes)
		print en2+sp1+"      MESSAGE SENT"
		delay()
	except:
		print "ERROR"

def addassi():
	os.system('clear')
	print en1+sp1+"     ADD ASSIGNMENT "
	print en2+sp2+"ENTER DEADLINE(yyyy-mm-dd): ",
	st=raw_input()
	p=data.cursor()
	p.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema='itws' AND table_name='sbase'")
	z=p.fetchall()
	noas=z[0][0]/3
	st1="ASSIGN"+str(noas)
	st2="DEAD"+str(noas)
	st3="mark"+str(noas)
	sd="ALTER TABLE sbase ADD COLUMN %s VARCHAR(256) DEFAULT 'PENDING'" %(st1)
	sf="ALTER TABLE sbase ADD COLUMN %s DATE DEFAULT '%s'" %(st2,st)
	sg="ALTER TABLE sbase ADD COLUMN %s INT DEFAULT 0" %(st3)
	p.execute(sd)
	p.execute(sf)
	p.execute(sg)
	print en2+sp1+"    ASSIGNMENT ADDED"
	delay()

def alterdead():
	os.system('clear')
	p=data.cursor()
	ch=assignmentselectadmin(p)
	print en2+sp2+"ENTER DEADLINE(yyyy-mm-dd): ",
	st=raw_input()
	stt="DEAD"+str(ch)
	st1="UPDATE sbase SET %s = '%s'" %(stt,st)
	p.execute(st1)
	print en2+sp1+"    DEADLINE MODIFIED"
	data.commit()
	delay()

def viewsubmission():
	os.system('clear')
	print en1+sp1+" LOGGED IN AS ADMINISTRATOR"
	print sp1+    "---------------------------"
	print en2+sp1+"ENTER ROLLNUMBER: ",
	x=int(raw_input())
	p=data.cursor()
	res=0
	comm=""
	p.execute("SELECT COUNT(*) FROM sbase WHERE ROLLNO=%s",(x,))
	res=p.fetchall()
	while(res[0][0]==0):
		print en2+sp1+"  ROLL NUMBER DOES NOT EXIST"
		delay()
		os.system('clear')
		print en1+sp1+" LOGGED IN AS ADMINISTRATOR"
		print sp1+    "---------------------------"
		print en2+sp1+"ENTER ROLLNUMBER: ",
		x=int(raw_input())
		p.execute("SELECT COUNT(*) FROM sbase WHERE ROLLNO=%s",(x,))
		res=p.fetchall()
	os.system('clear')
	print en1+sp1+"      1.READ SUBMISSION\n"
	print en2+sp1+"       2.ASSIGN MARKS\n"
	print en2+sp1+"     ENTER CHOICE:",
	y=int(raw_input())
	if(y==1):
		ch=100000
		p.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema='itws' AND table_name='sbase'")
		z=p.fetchall()
		noas=z[0][0]/3
		ch=assignmentselectadmin(p)
		while(ch<1 or ch>noas-1):
			print en2+sp2+" WRONG CHOICE"
			ch=assignmentselectadmin(p)
		fn="/home/anirudh/itwsfiles/submissions/"+str(x)+"/assign"+str(ch)+".txt"
		delay()
		try:
			fd=open(fn,"r")
			webbrowser.open(fn)
		except:
			print en2+sp1+"NO SUBMISSIONS YET"
			delay()
	elif(y==2):
		ch=assignmentselectadmin(p)
		os.system('clear')
		print en1+sp1+"   ENTER MARKS :",
		mar=int(raw_input())
		change="mark"+str(ch)
		if(ch==1):
			p.execute("""UPDATE sbase SET mark1 = %s WHERE ROLLNO = %s""",(mar,x))
		elif(ch==2):
			p.execute("""UPDATE sbase SET mark2 = %s WHERE ROLLNO = %s""",(mar,x))
		elif(ch==3):
			p.execute("""UPDATE sbase SET mark3 = %s WHERE ROLLNO = %s""",(mar,x))
		elif(ch==4):
			p.execute("""UPDATE sbase SET mark4 = %s WHERE ROLLNO = %s""",(mar,x))
		elif(ch==5):
			p.execute("""UPDATE sbase SET mark5 = %s WHERE ROLLNO = %s""",(mar,x))
		data.commit()

def printmainmenu():
	os.system('clear')
	print en1+sp1+"ASSIGNMENT SUBMISSION SYSTEM"
	print sp1+"----------------------------\n\n"
	print sp1+"  1.ENTER AS ADMINISTRATOR\n"
	print sp1+"     2.ENTER AS STUDENT\n"
	print sp1+"      3.CREATE ACCOUNT\n\n"
	print sp1+"     ENTER CHOICE:",
	x=int(raw_input())
	return x
	

data = MySQLdb.connect("127.0.0.1","root","anirudh1919","itws" )


while(True):

	a=printmainmenu()

	os.system('clear')

	if(a==1):
		acceptad()
		while(True):    			
			b=printadminmenu()
    			if(b==1):
    				viewsubmission()
				delay()
    			elif(b==2):
    				sendmess()
				delay()
    			elif(b==3):
    				addassi()
				delay()
    			elif(b==4):
    				alterdead()
				delay()
    			elif(b==5):
    				copy()
				delay()
			else:
				break
	elif(a==2):
		n=acceptstud()
		while(True):
			cho=printstudmenu(n)
			if(cho==1):
				subass(n)
				delay()
			elif(cho==2):
				readmess()
				delay()
			elif(cho==3):
				os.system('clear')
				viewmarks(n)
				delay()
			else:
				break
	elif (a==3):
		createstudent()
	else:
		print en1+sp2+ "        THANK YOU"
		break