from bson.objectid import ObjectId
from pymongo import ReturnDocument
from modules.application.repository import ApplicationRepository
from .comment_model import CommentModel

class CommentRepository(ApplicationRepository):
    collection_name = CommentModel.get_collection_name()

    @classmethod
    def create_comment(cls, comment_data: dict):
        query = cls.collection().insert_one(comment_data)
        return cls.collection().find_one({"_id": query.inserted_id})

    @classmethod
    def get_comments_by_task_id(cls, task_id: str):
        return list(cls.collection().find({"task_id": task_id}))

    @classmethod
    def update_comment(cls, comment_id: str, updated_fields: dict):
        return cls.collection().find_one_and_update(
            {"_id": ObjectId(comment_id)},
            {"$set": updated_fields},
            return_document=ReturnDocument.AFTER,
        )

    @classmethod
    def delete_comment(cls, comment_id: str):
        return cls.collection().delete_one({"_id": ObjectId(comment_id)})
