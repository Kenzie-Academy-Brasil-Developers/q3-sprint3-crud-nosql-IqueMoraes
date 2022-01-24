from flask import jsonify, request
from http import HTTPStatus
from app.models.post_class import Post as Post_class


def insert_new_post() -> any:
    try:
        data = request.get_json()

        if False in [bool(value) for value in data.values()]:
            return {"msg": "Não deixe valores vazios nas chaves do corpo da requisição."}, HTTPStatus.BAD_REQUEST

        new_post = Post_class(**data)
        new_post.create_post()
        Post_class.serialize_objectid(new_post)

        return jsonify(new_post.__dict__), HTTPStatus.CREATED


    except KeyError as e:
        return {"msg": "Verique as chaves no corpo da requisição. As chaves necessárias são: 'title', 'author', 'content', 'tags'.",
        "falta": e.args}, HTTPStatus.BAD_REQUEST