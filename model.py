from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

class EmployeeModel(db.Model):
    __tablename__ = "details"
 
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    phone = db.Column(db.Integer())
    position = db.Column(db.String(80))
    email = db.Column(db.String())
    gender = db.Column(db.String())
    dob = db.Column(db.Date())
 
    def __init__(self, employee_id,name,phone,position,email,gender,dob):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.position = position
        self.email = email
        self.gender =  gender
        self.dob = dob
        
 
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"