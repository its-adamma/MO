"""Model for Mask Request App"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
app = Flask(__name__)


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    fname = db.Column(db.String, nullable = False)
    lname = db.Column(db.String, nullable = False)
    email = db.Column(db.String(50), unique= True, nullable = False)
    password = db.Column(db.String(50),nullable = False)
    # joined_date = db.Column(db.DateTime)
    can_view_records = db.Column(db.Boolean, default=False)
    
    
    requests = db.relationship("Request")
    
    def __repr__(self):
        return f'<User fname={self.fname} user_id={self.user_id} email={self.email}>'

class Admin(db.Model):
    """Admin user"""

    __tablename__ = "admin"

    admin_id = db.Column(db.Integer,autoincrement= True, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey ("users.user_id"))
    request_id = db.Column(db.Integer, db.ForeignKey ("requests.request_id"))
    
    user = db.relationship("User")
    requests = db.relationship("Request")

class MaskType(db.Model):
    ""
    __tablename__ = "mask_types"
    
    mask_id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    mask_type = db.Column(db.String)
    reusable = db.Column(db.Boolean)
    valve = db.Column(db.Boolean)
    
    requests = db.relationship("Request")
    
    
class Request(db.Model):
    
    __tablename__ = "requests"
    
    request_id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey ("users.user_id"))
    mask_id = db.Column(db.Integer, db.ForeignKey ("mask_types.mask_id"))
    num_packs = db.Column(db.Integer)
        
    user = db.relationship("User")
    mask_type = db.relationship("MaskType")
    
    def __repr__(self):
        return f'<Request request_id={self.request_id} user_id={self.user_id} num_packs={self.num_packs}>'

def connect_to_db(app):
    """Connect db to flask app"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///maskoakland"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to db")   