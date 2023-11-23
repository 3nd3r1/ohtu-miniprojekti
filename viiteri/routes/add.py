# pylint: disable=import-error, no-name-in-module, broad-except

""" viiteri/routes/create_reference.py """
from flask import Blueprint, render_template, redirect, request, flash, session
from viiteri.services.reference_service import reference_service


blueprint = Blueprint("add", __name__)


@blueprint.route("/add", methods=["GET", "POST"])
def add_reference():
    """ Render page for adding a new reference """
    if request.method == "GET":
        submitted = session.pop('submitted', False)
        return render_template("add.html", submitted=submitted)
    if request.method == "POST":
        cite_key = request.form["title"][0:3] + request.form["author"].split(" ")[0][0:3]
        try:
            reference_service.create_reference(cite_key=cite_key, **request.form.to_dict())
            flash("Reference created successfully!")
            session["submitted"] = True
        except Exception as error:
            flash(str(error))
            print(str(error))
            session["submitted"] = False
    return redirect("/add")