from flask import Blueprint, render_template

triplebyte_module = Blueprint('tiplebyte', __name__, url_prefix='/triplebyte')

@triplebyte_module.route('/')
def triplebyte():
    return render_template('triplebyte/index.html')