# what do you want to disp in app, write cruf fun for that
# mask types 
#limit in cart of masks

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

# def delete_user(user_id):
#     """Delete user from database"""
    
#     print(f'Deleting user from system:')
    
#     user_id = User.query.filter_by(user_id).one()
    
#     User.query.filter(User.user_id == user_id).delete()
        
#     db.session.delete(user_id)
#     db.session.commit()

def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by user_id"""

    return User.query.get(user_id)
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
    
# create_mask_type(mask_type="n95", img_url="/static/n95_respirator.png", mask_test="Cleared by the U.S. Food and Drug Administration (FDA)",reusable=False,valve=False, fit="Loose-fitting", filtration="Does NOT provide the wearer with a reliable level of protection from inhaling smaller airborne particles and is not considered respiratory protection", limitation="Disposable. Discard after each patient encounter.")



# create_user(fname="Tam",lname="LBrr", phone=443445, email="tam@gmail.com", password="pw")


# create_request(request_id,user_id, mask_id, healthcare_center, address,num_packs)