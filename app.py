import sqlite3
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# CONF FOLDER PATH DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airport.db'
db = SQLAlchemy(app)

#Conn table flights
class Flights(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String(80), nullable=False)
	destination = db.Column(db.String(80), nullable=False)
	duration = db.Column(db.Integer, nullable=False)

# Con TABLE PASSAGERS 
class Passengers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	flight_id = db.Column(db.Integer)


#conn = sqlite3.connect('airport.db')
#cursor = conn.cursor()

# Select tabela
#cursor.execute(" Select id, origin, destination, duration from flights ")
#count = cursor.fetchall()

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/flights")
def flights_registered_db():
	flights = Flights.query.all()
	passengers = Passengers.query.all()
	return render_template('flights.html', flights=flights, passengers=passengers)

@app.route("/flights/<int:flight_id>")
def  flights_detail(flight_id):
	flights = Flights.query.filter_by(id=flight_id)

	passengers = Passengers.query.filter_by(flight_id=flight_id)
	return render_template("flights_detail.html", flights=flights, passengers=passengers)		

@app.route("/register")
def register():
	return render_template("register_flights.html")

@app.route("/passengers")
def passagers_view():
	flights = Flights.query.all()
	
	return render_template("passagers_register.html", flights=flights)


@app.route("/imput-flights", methods=['POST'])
def flights_regist_db():
	flights_register = Flights(origin=request.form['Origin'], destination=request.form['Destination'], 
		duration=request.form['Duration'])

	db.session.add(flights_register)
	db.session.commit()
	return redirect(url_for('homepage'))

@app.route("/imput-passengers", methods=['POST'])
def passengers_regist_db():
	
	passengers_register = Passengers(name=request.form['Name'], flight_id=request.form['flight_id'])
	db.session.add(passengers_register)
	db.session.commit()
	return 'save'



@app.route("/delete/<id>")
def delete(id):
	flight = Flights.query.filter_by(id=int(id)).delete()
	db.session.commit()
	return redirect(url_for('homepage'))

#conn.close()
 
if (__name__ == "__main__"):
    #app.run(port = 5000)
    app.run(debug = True)
