from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_myBoard():
    return ">> hello, myBoard"

@bp.route('/')
def index():
    return 'myBoard index'