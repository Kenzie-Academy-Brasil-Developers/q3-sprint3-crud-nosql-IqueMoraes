# from app import controllers as controller
from app.controllers.create_controller import insert_new_post
from app.controllers.update_controller import updating_post
from app.controllers.read_controller import reading_posts
from app.controllers.delete_controller import deleting_post




def posts_route(app) -> tuple:

    @app.get("/posts")
    def read_posts():
        # return controller.read_post()
        return reading_posts()

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        # return controller.read_post(id)
        return reading_posts(id)

    @app.post("/posts")
    def create_post():
        # return controller.create_post()
        return insert_new_post()

    @app.patch("/posts/<int:id>")
    def update_post(id):
        # return controller.update_post(id)
        return updating_post(id)

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        # return controller.delete_post(id)
        return deleting_post(id)
