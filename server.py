"""Masks on Demand appl Flask server

Browse masks, view details, and to wishlist
"""

from flask import Flask, render_template, redirect, flash, session, jsonify

import jinja2
import masks

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
    """Return About US page"""

    return render_template("about_us.html")


@app.route("/masks")
def list_masks():
    """Return page showing all the masks ubermask has to offer"""

    mask_list = masks.get_all()
    return render_template("all_masks.html",
                           mask_list=mask_list)


@app.route("/mask/<mask_id>")
def show_mask(mask_id):
    """Return page showing mask details with button to add masks to wishlist
    """

    mask = masks.get_by_id(mask_id)
    print(mask)
    return render_template("mask_details.html",
                           display_mask=mask)


@app.route("/request")
def display_request():
    """Display content of request."""

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

    return render_template("request.html",
                           mask_objects=mask_objects, request_total_cost=request_total_cost)


@app.route("/add_to_request/<mask_id>")
def add_to_request(mask_id):
#     """Add a mask to wishlist request and redirect to wishlist request page.

#     When a mask is added to the request, redirect browser to wishlist page and display a confirmation message


    # check if wishlist requests exists in the sessionand create one (empty
    # dict keyed to the string "request") if not
    # check if the desired mask id is the request, and if not, put it in
    # increment count for that mask id by 1
    # flash a success message
    # redirect the user to the request page

    session['request'] = session.get('request', {})

    session['request'][mask_id] = session['request'].get(mask_id, 0) + 1

    flash('mask successfully added to request!')

    return redirect("/request")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    user's login credentials located in the 'request.form'
    dictionary
    look up the user
    store them in the session.
    """

    return "⚠️ Please check back again later"


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

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")
