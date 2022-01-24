from flask import Flask, Response, request
from app.controllers import create_controller




def posts_route(app) -> tuple:

    @app.get("/posts")
    def read_posts():
        pass

        # return controllers.reading_all_posts()

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        pass


    @app.post("/posts")
    def create_post():
        return create_controller.insert_new_post()


    @app.patch("/posts/<int:id>")
    def update_post(id):
        pass

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        pass
