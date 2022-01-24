from http import HTTPStatus
from flask import jsonify
from app.models.post_class import Post as Post_class


def reading_posts(id: int = None):
    try:
        posts_list = list(Post_class.get_posts(id))
        Post_class.serialize_objectid(posts_list)
        if id and not posts_list:
            return {"msg": "Não há nenhum post com o id indicado."}, HTTPStatus.NOT_FOUND
        else:
            return jsonify(posts_list), HTTPStatus.OK
    
    except Exception as e:
        return jsonify(e.args[0]), HTTPStatus.INTERNAL_SERVER_ERROR
