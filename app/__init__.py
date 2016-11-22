from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from app.about import about_module as mod_about
from app.projects import projects_module as mod_projects
app.register_blueprint(mod_about)
app.register_blueprint(mod_projects)

