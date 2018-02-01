from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template ('home.html')
	

@app.route('/categories')
def categories():
	return render_template ('categories.html')
	

@app.route('/add')
def add():
    return render_template ('add.html')


# @app.route('/post_contact')
# def post_contact():
#     return render_template ('post-contact.html')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
heroku = Heroku(app)

db = SQLAlchemy(app)
class info(db.Model):
	__tablename__ = "info"
	id = db.Column(db.Integer, primary_key=True)
	First_Name = db.Column('First Name', db.Unicode)
	Last_Name = db.Column('Last Name', db.Unicode)
	Country = db.Column('Country', db.Unicode)
	Subject = db.Column('Subject', db.Unicode)
db.create_all()

@app.route('/post_contact', methods=['POST'])
def submit_form():
	First_Name = request.form["firstname"]
	Last_Name = request.form["lastname"]
	Country = request.form["country"]
	Subject = request.form["subject"]
	Email = request.form["email"]

	contact_info = info(First_Name=First_Name,Last_Name=Last_Name, Country=Country, Subject=Subject ) 
	db.session.add(contact_info)
	db.session.commit()
	return render_template ('post-contact.html')
