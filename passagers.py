from flask_sqlalchemy import SQLAlchemy
import app 

# CONF FOLDER PATH DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airport.db'
db = SQLAlchemy(app)

class Passager(db.Model):
	Passagers.id = db.Column(Integer, primary_key=True)
	Passagers.name = db.Column(String)
	Passagers.flights = db.Column(Integer)

	

