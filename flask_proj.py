#!/usr/bin/env python

import os
from flask_migrate import Migrate, upgrade
from app import create_app, db
from dotenv import load_dotenv
from app.models import Task, User, Role, Permission, Post, Comment, Like, Notification


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post, Comment=Comment,
                Like=Like, Rol=Role, Permissio=Permission, Notification=Notification, Task=Task)


@app.cli.command("deploy")
def deploy_app():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    # create or update user roles
    Role.insert_roles()
