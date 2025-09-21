import os
from flask import Blueprint, jsonify,request
from app.models import Student
from app.db import db
import re

# setting the initial bluepring
student_bp= Blueprint("student",__name__)
@student_bp.route("/",methods=["GET"])
def homepage():
    print("Welcome to our site")
    return "Homepage activated"
# adding the students using json method
@student_bp.route("/add/json",methods=["POST"])         
def add_student():
    data= request.get_json()
    name= data.get("name")
    email= data.get("email")

    if not name:
        return jsonify({"error":"Name is required"}),400
    
    if not email:
        return jsonify({"error":"Email is required"}),400
    # validates wheather th email is inthe correct format
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex,email):
        return jsonify({"error":"Invalid email address"})
    
   # checks wheather the email exists in the database
    exist= Student.query.filter_by(email=email).first()
    if exist:
        return jsonify({"erro":"Email in use"})
    new_student= Student(name=name,email=email)

#   adding the students to the database
    db.session.add(new_student)
    db.session.commit()
    return jsonify({
        "message":"Student added",
        "id":new_student.id,
        "name":new_student.name,
        "email":new_student.email
    })
# reading the student data from the datbase
@student_bp.route("/read",methods= ["GET"])
def read_data():
    # getting all the  students 
    students= Student.query.all()
    data= [ ]
    for student in students:
        data.append(
        {"id":student.id,
        "name":student.name,
        "email":student.email
        }
        )

    return jsonify({
        "students":data,
        "count": len(data)
    }),
# updating the student data using dynamic routes
@student_bp.route("/update/<int:id>",methods=["PUT"])
def update_student(id):\
# getting the student by the id
    student_id= Student.query.get(id)
    if not student_id:
        return jsonify({"message":f"student with {id} does not exist"})
    data= request.get_json()
    if "name" in data:
        student_id.name=data["name"]
    if "email" in data:
        student_id.email=data["email"]
    db.session.commit()
    return jsonify({
        "message":"Student added",
        "id":student_id.id,
        "name":student_id.name,
        "email":student_id.email
    })
# adding students via form 
@student_bp.route("/add/form",methods=["POST"])
def form_student():
    data=request.form
    name= data.get("name")
    email=data.get("email")
    new_student=Student(name=name,email=email)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({
        "message":"Form data added",
        "name":new_student.name,
        "email":new_student.email

    })
# deleteing students from the database using dynamic routes
@student_bp.route("/delete/<int:id>",methods=["DELETE"])
def delete_student(id):
    student_id= Student.query.get(id)
    if not student_id:
        return jsonify({"message":f"student with {id} does not exist"})
    db.session.delete(student_id)
    db.session.commit()
    return jsonify({
        "message":"Student deleted"        
    })