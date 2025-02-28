from . import db
from flask_login import UserMixin
import enum
from sqlalchemy.sql import func
from sqlalchemy import Enum, Column
import typing

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_status = db.Column(db.String(100))
        
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(150))
    company = db.Column(db.String(100))
    
class JobType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_type: Column = db.Column(db.String(50))
    
class LocationType(enum.Enum):
    remote = "Remote"
    hybrid = "Hybrid"
    on_site = "On Site"
    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    location_type = db.Column(Enum(LocationType))
    
class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_company = db.Column(db.String(150))
    job_listing = db.Column(db.Text)    
    job_listing_url = db.Column(db.String(1000))
    resume = db.Column(db.String(256))
    job_type_id = db.Column(db.Integer, db.ForeignKey('job_type.id'))
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contact.id"))
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"))
    updated = db.Column(db.DateTime(timezone=True), default=func.now())
    
class JobApplicationAudit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer)
    contact_id = db.Column(db.Integer, db.ForeignKey("contact.id"))
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"))
    updated = db.Column(db.DateTime(timezone=True))