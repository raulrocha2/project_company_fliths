import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


conn = sqlite3.connect('/home/raul_mint/Documents/curso_python/flask01/Flask_DB/airport.db')
cursor = conn.cursor()

# Select tabela
cursor.execute(" Select id, origin, destination, duration from flights ")
count = cursor.fetchall()

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/voos")
def Select():

	for tb in count:
		tb_list = tb
		context ={
		'tb_list': tb_list
		}
		print (context)

	return render_template("select.html", context=context)





conn.close()
 
if (__name__ == "__main__"):
    #app.run(port = 5000)
    app.run(debug = True)

