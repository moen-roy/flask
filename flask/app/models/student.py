from app.db import db

class Student(db.Model):
    __tablename__="student"
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50),unique= True,nullable=False)
    email= db.Column(db.String(50),unique= True,nullable=False)
