from flask import request, render_template, redirect, Blueprint
from flask_login import current_user

from db import db
from models.form import ConnectForm

connect = Blueprint('connect', __name__)


@connect.route('/connect', methods=['GET', 'POST'])
def connect_services():
    form = ConnectForm(obj=current_user)

    if request.method == 'POST' and form.validate():
        form.populate_obj(current_user)
        db.session.commit()
        return redirect("/")
    return render_template('connect.html', form=form)
