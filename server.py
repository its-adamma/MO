"""Masks on Demand app Flask server

Browse masks, view details, and to wishlist
"""

from flask import Flask, render_template, redirect,request, flash, session, jsonify

import jinja2
import crud

app = Flask(__name__)


app.secret_key = " "

app.jinja_env.undefined = jinja2.StrictUndefined


app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def index():
    """Return homepage"""

    return render_template("homepage.html")

@app.route("/about")
def view_about():
    """Return About Us page"""

    return render_template("about_us.html")


@app.route("/masks")
def list_masks():
    """Return page showing all the masks offered"""
    
    mask_list = crud.get_masks()
    return render_template("all_masks.html",
                        mask_list=mask_list)
    
@app.route("/all_masks_s")
def list_masks_from_db():
    """Return page showing all the masks offered"""

    mask_list = crud.get_masks()
    return render_template("all_masks_s.html",
                        mask_list=mask_list)
    
    
@app.route("/all_users")
def list_users():
    """Return page showing all users"""

    users = crud.get_users()
    return render_template("all_users.html",
                        users=users)


@app.route("/mask/<mask_id>")
def show_mask(mask_id):
    """Return page showing mask details with button to add masks to wishlist
    """

    mask = crud.get_mask_by_id(mask_id)
    print(mask)
    return render_template("mask_details.html",
                        mask=mask)


@app.route("/requests")
def display_request():
    """Display all requests"""

    request_contents = session.get('request', {})
    mask_objects = []
    request_total_cost = 0

    for key in request_contents:
        request_mask = masks.get_by_id(key)
        request_total_cost += (request_mask.price * request_contents[key])
        setattr(request_mask, "price", request_contents[key])
        setattr(request_mask, "total_cost",
                (request_mask.price * request_contents[key]))
        mask_objects.append(request_mask)

    return render_template("requests.html",
                        mask_objects=mask_objects, 
                        request_total_cost=request_total_cost)

@app.route("/make_mask", methods=["GET"])
def show_mask_form():
    """Show make mask form."""

    return render_template("make_mask.html")
        
@app.route("/make_mask", methods=["POST"])
def process_make_mask_form():
    """ """
    mask_type = request.form.get("mask_type")
    img_url = request.form.get("img_url")
    mask_test = request.form.get("mask_test")
    reusable = False
    valve = False
    fit = request.form.get("fit")
    filtration = request.form.get("filtration")
    limitation = request.form.get("limitation")
    
    crud.create_mask_type(mask_type, img_url, mask_test,reusable,valve, fit, filtration, limitation)

    return redirect("/masks")

@app.route("/make_request", methods=["POST"])
def make_request():
    """User makes a request (wishlist)"""
    mask_id = request.form.get("mask_id")
    user_id = session["user_id"]
    
    print(f"User ID = {user_id}")
    
    crud.create_request(user_id,mask_id)
    
    flash('Your request has been received!')
    
    return redirect("/masks")


@app.route("/make_request_ajax", methods=["POST"])
def make_request_ajax():
    """"""
    mask_id = request.form.get("mask_id")
    user_id = session["user_id"]
    
    print(f"User ID = {user_id}")
    
    crud.create_request(user_id,mask_id)
    
    return "Your request has been received!"

@app.route("/view_wishlist", methods=["GET"])
def view_wishlist():
    """Show items in wishlist."""
    
    user_id = session["user_id"]
    
    user = crud.get_user_by_id(user_id)

    return render_template("view_wishlist.html", user = user)



# ------LOGIN -----------

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    """Log user into application."""

    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)

    if password == user.password:   
        session["user_id"] = user.user_id
        flash(f'Logged in as {email}')
        return redirect('/masks')
    else:
        flash('Wrong password!')
        return redirect('/login')


@app.route("/delivery_total_conc")
def view_mask_total():
    """Return Mask Delivery total by mask type"""

    return render_template("delivery_total_conc.html")

if __name__ == "__main__":
    crud.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    



















    
#     # query db to see if emal & pw valid user
#     #session["user_id"]=user.user_id

#     return "⚠️ Please check back again later"

# @app.route("/checkout")
# def checkout():
#     """Checkout customer and deliver masks."""


#     flash("Your request is being processed")
#     return redirect("/masks")


# @app.route('/session')
# def set_session():

#     session['request'] = {'mask': 1}

#     fav_num = session['request']['mask']

#     return f"""<html><p>{fav_num}</p></html>"""

# @app.route('/logout')
# def process_logout():
#     """Log healthcare user out of session and delete session key"""

#     del session['logged_in_healthcare_user_email']
#     flash('Your arelogged out!')
#     return redirect("/masks")

