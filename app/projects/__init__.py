from flask import Blueprint, render_template

projects_module = Blueprint('projects', __name__, url_prefix='/projects')

@projects_module.route('/')
def projects():
    return render_template('projects/index.html')