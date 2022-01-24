from ipdb import set_trace
from http import HTTPStatus
from flask import jsonify
from app.models.post_class import Post as Post_class


def deleting_post(id: int):
    try:
        deleted_post = Post_class.del_post(id)
        if not deleted_post:
            raise TypeError
        Post_class.serialize_objectid(deleted_post)

        return jsonify(deleted_post), HTTPStatus.OK
    
    except TypeError:
        return {"msg": "Não há nenhum post com o id indicado como parâmetro."}, HTTPStatus.NOT_FOUND
        