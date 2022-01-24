from ipdb import set_trace
from http import HTTPStatus
from flask import request, jsonify
from app.models.post_class import Post as Post_class


def updating_post(id: int) -> any:
    data = request.get_json()
    valid_keys = ['title', 'author', 'content', 'tags']

    if False in [bool(value) for value in data.values()]:
        return {"msg": "Não deixe valores vazios nas chaves do corpo da requisição."}, HTTPStatus.BAD_REQUEST

    if False in [key in valid_keys for key in data.keys()]:
        return {"msg": "Chave inválida no corpo da requisição. As chaves válidas são: {}.".format(valid_keys)}, HTTPStatus.BAD_REQUEST
    
    
    if Post_class.update_post(id, **data):
        updated_post = list(Post_class.get_posts(id))
        print(updated_post)
        Post_class.serialize_objectid(updated_post)
        print(updated_post)

        return jsonify(updated_post), HTTPStatus.OK

    else:
        return {"msg": "Não há nenhum post com o id indicado no parâmetro. Verifique o endereço da requisição."}, HTTPStatus.NOT_FOUND

