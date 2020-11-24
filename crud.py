# what do you want to disp in app, write cruf fun for that
# mask types 
#limit in cart of masks

"""CRUD operations"""

from model import db, User, MaskType, Request, connect_to_db

# ----------------------REQUESTS-------------------

def get_users():
    """Return all users."""

    return User.query.all()

def create_user(fname, lname, email, password, can_view_records):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password,can_view_records=can_view_records)

    db.session.add(user)
    db.session.commit()

    return user

# ----------------------REQUESTS-------------------
def get_requests():
    """Return all requests."""

    return Request.query.all()

def create_request(request_id,
                   user_id, 
                   mask_id, 
                   num_packs):
    
    """Create and return a request"""

    request = Request(request_id=request_id,
                  user_id=user_id,
                  mask_id=mask_id,
                  num_packs=num_packs)

    db.session.add(request)
    db.session.commit()

    return request


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
