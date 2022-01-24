from flask import Flask
from app import views as posts_views

def create_app() -> None:

    app = Flask(__name__, static_folder=None)

    posts_views.init_app(app)

    return app
