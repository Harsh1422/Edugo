from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/')
def login():
    return "<h1> WTF </h1>"