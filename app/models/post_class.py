import pymongo
import datetime


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
        self.created_at = self.created_date()
        self.updated_at = ""


    def id_taken(self) -> int:
        response = list(db.get_collection(collection).find())
        if bool(response):
            response.sort(key=lambda a: a['id'], reverse=True)
            return response[0]['id'] + 1
        else:
            return 1

    def created_date(self) -> None:
        return datetime.datetime.now().isoformat()

    def update_date(self) -> None:
        self.update_at = datetime.datetime.now()

    def create_post(self) -> None:
        db.get_collection(collection).insert_one(self.__dict__)
    
    @staticmethod
    def serialize_objectid(data):
        if type(data) is list:
            for post in data:
                post.update({"_id": str(post["_id"])})
        elif type(data) is Post:
            data._id = str(data._id)
        elif type(data) is dict:
            data.update({"_id": str(data["_id"])})

    


    @staticmethod
    def get_posts() -> list:
        posts_list = db.get_collection(collection).find()

