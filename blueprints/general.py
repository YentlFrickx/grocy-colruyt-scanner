from flask import Blueprint, render_template
from flask_login import login_required, current_user

general = Blueprint('general', __name__)


@general.route("/")
@login_required
def index():
    return render_template('home.html', grocy_key=current_user.grocy_api_key)
