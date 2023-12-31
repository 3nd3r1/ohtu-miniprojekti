""" viiteri/routes/create_reference.py """

from flask import Blueprint, render_template, redirect, request, flash, session
from sqlalchemy.exc import SQLAlchemyError

from viiteri.services.reference_service import reference_service


blueprint = Blueprint("add", __name__)

@blueprint.route("/")
@blueprint.route("/add", methods=["GET", "POST"])
def add_reference():
    """ Render page for adding a new reference """
    if request.method == "GET":
        doi = request.args.get("doi_fill")
        doi_data = None
        last_ref_type = session.get("last_ref_type", "article")
        if doi:
            try:
                doi_data = reference_service.get_reference_by_doi(doi)
                last_ref_type = doi_data['ENTRYTYPE']
            except ValueError as error:
                flash(str(error), "error")
            except TimeoutError as error:
                flash(str(error), "error")
        return render_template("add.html", last_ref_type=last_ref_type, doi_data=doi_data)
    if request.method == "POST":
        ref_type = request.form.get("ref_type")
        try:
            cite_key = request.form["title"][0:3] + \
                request.form["author"].split(" ")[0][0:3]
            reference_service.create_reference(
                ref_type, cite_key=cite_key, **request.form.to_dict())
            flash("Reference created successfully!", "success")
            session["last_ref_type"] = ref_type
        except SQLAlchemyError:
            flash("Database failed to add reference", "error")
        except ValueError as error:
            flash(str(error), "error")
    return redirect("/add")
