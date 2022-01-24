from app.views.posts_route import posts_route
from flask import Flask

def init_app(app):
    
    posts_route(app)