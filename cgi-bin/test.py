#!/usr/bin/python
import csv
import sys
import cgi,cgitb
import pico
#user_data = sys.argv[1:]
cgitb.enable()
i = 0
d = 0
count = 0
form = cgi.FieldStorage()
user_data=form.getvalue('searchbox')
string = ''

def test():
	Check_after=5
	count2=count-5
	#for i in range(1,trigger):
	with open("infy.csv","rb") as out:
		data=csv.reader(out,delimiter=',')
		data = [row for row in data]
		ext = data[count2]
		#print(ext)
		check_value=ext[1]

	if (check_value > user_data):
		#print("increment")
		global i
		i+=1
	else: 
		#print("decrement")
		global d
		d+=1
	out.close
#print(increment,decrement)


def stockvaluetest():
	
	with open("infy.csv","rb") as out:
		data=csv.reader(out,delimiter=',')
			

		for row in data:
			#for val in row:
				#print(row[1])
				if (user_data == row[1]):
					#print(row)
					#print("User value found at line no.:",count)
					#break
					#trigger+=1
					test()
				else:
					global count
					count +=1
	out.close


	if(i>d):
		global string
		string = "Increment"
	elif(d>i):
		global string
		string = "Decrement"
	else:
		global string
		string = "The company's stock hasn't had this value in some time."
	return string
print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title> Test Value </title>")
print("</head>")
print("<body>")
print(stockvaluetest())
print("</body>")
print("</html>")


#print(count)
