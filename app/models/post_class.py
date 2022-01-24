
import pymongo
import datetime
from ipdb import set_trace


url = "mongodb://localhost:27017/"
db_name = "kenzie"
client = pymongo.MongoClient(url)
db = client[db_name]
collection = "posts"


class Post:

    def __init__(self, **kwargs) -> None:
        self.title = kwargs['title'].title()
        self.author = kwargs['author'].title()
        self.content = kwargs['content']
        self.tags = [tag.lower() for tag in kwargs['tags']]
        self.id = self.id_taken()
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = ""


    def id_taken(self) -> int:
        response = list(db.get_collection(collection).find())
        if bool(response):
            response.sort(key=lambda a: a['id'], reverse=True)
            return response[0]['id'] + 1
        else:
            return 1


    def create_post(self) -> None:
        db.get_collection(collection).insert_one(self.__dict__)

    
    @staticmethod
    def update_post(id: int, **kwargs) -> None:
        update_date = datetime.datetime.now().isoformat()
        kwargs.update({"updated_at": update_date})
        return db.get_collection(collection).find_one_and_update({"id": id}, {"$set":kwargs})
        

    
    @staticmethod
    def serialize_objectid(data) -> None:
        if type(data) is list:
            for post in data:
                post.update({"_id": str(post["_id"])})
        elif type(data) is Post:
            data._id = str(data._id)
        elif type(data) is dict:
            data.update({"_id": str(data["_id"])})



    @staticmethod
    def get_posts(id: int = None) -> list:
        filter_key = {"id": id}
        if id:
            return db.get_collection(collection).find(filter_key)
        else:
            return db.get_collection(collection).find()

    @staticmethod
    def del_post(id: int):
        filter_key = {"id": id}
        return db.get_collection(collection).find_one_and_delete(filter_key)

    