
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,render_template
import re
from model import db,EmployeeModel
from datetime import datetime
from sqlalchemy import exc
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy()
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
# class EmployeeModel(db.Model):
#     __tablename__ = "details"
 
#     id = db.Column(db.Integer, primary_key=True)
#     employee_id = db.Column(db.Integer(),unique = True)
#     name = db.Column(db.String())
#     phone = db.Column(db.Integer())
#     position = db.Column(db.String(80))
#     email = db.Column(db.String())
 
#     def __init__(self, employee_id,name,phone,position,email):
#         self.employee_id = employee_id
#         self.name = name
#         self.phone = phone
#         self.position = position
#         self.email = email
 
#     def __repr__(self):
#         return f"{self.name}:{self.employee_id}"

@app.route("/")  
def index():
    return render_template("index.html")  

@app.route("/add_employee")  
def add():  
    return render_template("add_employee.html")  

@app.route('/enterdetails' , methods = ['GET','POST'])
def create():  
    try:
        msg = None
        err_msg = None
        def validateFields(employee):
            err_msg = None
            if not (re.match('[a-zA-Z\s]+$', employee.name)):
                err_msg = "Please enter name correctly"
            elif not (employee.employee_id.isalnum()):
                err_msg = "Please enter id correctly"
            elif not (employee.phone.isdigit()):
                err_msg = "Please enter digits for mobile no."
            elif len(employee.phone) != 10:
                err_msg = "Please enter 10 digits for mobile no."
            elif not (re.match('[a-zA-Z\s]+$', employee.position)):
                err_msg = "Please enter designation correctly"
            return err_msg
        employee_id = request.form['employee_id']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        position = request.form['position']
        gender = request.form['gender']
        date = request.form['date']
        dob = datetime.strptime(date, "%Y-%m-%d").date()
        employee = EmployeeModel(employee_id=employee_id, name=name, phone=phone, email=email, position = position,gender=gender,dob=dob)
        err_msg = validateFields(employee)
        if  not err_msg:
            db.session.add(employee)
            db.session.commit()
            msg = "Details Entered Successfully!" 

    # except Exception as e:
    #     msg = type(e) #"Enter unique id. This id is taken" 
    # except (DataError, IntegrityError) as e:
    #     msg =type(e) #"Enter unique id. This id is taken"
    # except (DataError, IntegrityError) as e:
    #     webhelpers.dbsession.rollback()
    #     raise 
    # except: 
    #     msg= "some other exception"
    except exc.IntegrityError as e:
        msg = "Enter unique id. This id is taken"
        # db.session.rollback()
    except :
        msg = "Something went wrong!"

    finally:
        return render_template("add_employee.html",msg=msg,err_msg=err_msg) 

@app.route('/view_list')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('view_list.html',employees = employees)

@app.route("/remove_employee")  
def delete():
    return render_template("remove_employee.html") 

@app.route('/deleteEntry', methods=['GET','POST'])
def deleterecord():
    msg = None
    if request.method == 'POST':



        id = request.form['id']
        employee = EmployeeModel.query.filter_by(employee_id=id).first()
        if employee:
            db.session.delete(employee)
            db.session.commit()
            msg = "record successfully deleted" 
        else:
            msg = "Can not delete"
    return render_template('remove_employee.html',msg = msg)