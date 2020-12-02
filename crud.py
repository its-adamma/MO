"""CRUD operations"""
from model import db, User, MaskType, Request, connect_to_db

import datetime


# ----------------------USERS-------------------

def get_users():
    """Return all users."""

    return User.query.all()

def create_user(fname, lname, phone, email, password):
    

    """Create and return a new user."""

    user = User(fname=fname, lname=lname, phone=phone,email=email, password=password)
    # date_created=datetime.datetime.now())
    
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by user_id"""

    return User.query.get(user_id)

# def delete_user(user_id):
#     """Delete user from database"""
    
#     print(f'Deleting user from system:')
    
#     user_id = User.query.filter_by(user_id).one()
    
#     User.query.filter(User.user_id == user_id).delete()
        
#     db.session.delete(user_id)
#     db.session.commit()

# ----------------------REQUESTS-------------------
def get_requests():
    """Return all requests."""

    return Request.query.all()

def create_request(user_id, 
                    mask_id): 
                    # healthcare_center,
                    # address,
                    # num_packs):
    
    """Create and return a request instance"""

    request = Request(user_id=user_id,
                    mask_id=mask_id)
                    # healthcare_center=healthcare_center,
                    # address=address,
                    # num_packs=num_packs)


    db.session.add(request)
    db.session.commit()

    return request    

def delete_request(request_id):
    """Delete request for the user"""
    Request.query.filter(Request.request_id == request_id).delete()
    db.session.commit()

# --------- MASKS --------
def get_masks():
    """Return all masks."""

    return MaskType.query.all()

def get_mask_by_id(mask_id):
    """Return mask"""

    return MaskType.query.get(mask_id)

def create_mask_type(mask_type, img_url, mask_test,reusable,valve, fit, filtration, limitation):
    

    
    masktype = MaskType(mask_type=mask_type,
                img_url=img_url,
                mask_test=mask_test,
                reusable=reusable,
                valve=valve,
                fit=fit,
                filtration=filtration,
                limitation=limitation)

    db.session.add(masktype)
    db.session.commit()

    return masktype

def delete_mask_type(mask_id):
    """Delete mask type from offering"""
    MaskType.query.filter(MaskType.mask_id == mask_id).delete()
    db.session.commit()
    
def view_mask(mask_id):
    """View one mask type"""
    
    mask = MaskType.query.get(mask_id)
    return mask

if __name__ == '__main__':
    from server import app
    connect_to_db(app)



