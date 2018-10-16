import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from .managers import TwilioManager

bp = Blueprint('twilio_handler', __name__, url_prefix='/sms')


@bp.route('/test', methods=('GET', 'POST'))
def test():
    twilio_mgr = TwilioManager.get_instance()

    return 'Sms Test!'