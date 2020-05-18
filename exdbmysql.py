import mysql.connector 
#as mariadb

mydb = mysql.connector.connect(user='root', password='wkz1045w', database='course_havard')

myconsult = mydb.cursor()

myconsult.execute("show tables")

for i in myconsult:
	print(i)
