from flask import Flask
# from flask_admin import Admin
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')
db = SQLAlchemy(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)
app = Flask(__name__)
app.config.from_object('config')

# Register Blueprints
from app.about.controllers import about_module as mod_about
from app.projects.controllers import projects_module as mod_projects
from app.triplebyte.controllers import triplebyte_module as mod_triplebyte
app.register_blueprint(mod_about)
app.register_blueprint(mod_projects)
app.register_blueprint(mod_triplebyte)
