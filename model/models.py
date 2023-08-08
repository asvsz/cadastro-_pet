# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tutor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  pets = db.relationship('Pet', backref='tutor', lazy=True)
  
class Pet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable=False)