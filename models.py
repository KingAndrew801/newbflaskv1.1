from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pets.db"
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    age = db.Column('Age', db.String())
    breed = db.Column('Breed', db.String())
    color = db.Column('Color', db.String())
    weight = db.Column('Weight', db.String())
    url = db.Column('URL', db.String())
    url_tag = db.Column('ALT TAG', db.String())
    pet_type = db.Column('Pet Type', db.String())
    gender = db.Column('Gender', db.String())
    spay = db.Column('Spay', db.String())
    housetrained = db.Column('Housetrained', db.String())
    description = db.Column('Description', db.Text())

    def __repr__(self):
        return f'''<Pet (Name: {self.name}
        Age: {self.age}
        Color: {self.color}
        Weight: {self.weight}
        URL: {self.url}
        Tag: {self.url_tag}
        Type: {self.pet_type}
        Gender: {self.gender}
        Spay: {self.spay}
        Housetrained: {self.housetrained}
        Description: {self.description})     
        '''
