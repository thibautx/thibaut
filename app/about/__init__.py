from flask import Blueprint, render_template

about_module = Blueprint('about', __name__, url_prefix='/about')

@about_module.route('/')
def about():
    return render_template('about/index.html')