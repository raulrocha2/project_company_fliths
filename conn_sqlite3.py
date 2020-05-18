import sqlite3

conn = sqlite3.connect('/home/raul_mint/Documents/curso_python/flask01/Flask_DB/airport.db')
cursor = conn.cursor()

# Select tabela
cursor.execute(" Select * from flights ")
count = cursor.fetchall()
for tb in count:
	print(tb)
	
conn.close()