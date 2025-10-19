from dataclasses import asdict
from modules.comments.internals.store.comment_repository import CommentRepository
from modules.comments.types import Comment, CreateCommentParams, UpdateCommentParams
from modules.comments.internals.store.comment_model import CommentModel

class CommentService:
    @staticmethod
    def create_comment(params: CreateCommentParams) -> Comment:
        comment_model = CommentModel(
            id=None,
            task_id=params.task_id,
            account_id=params.account_id,
            content=params.content
        )
        comment_bson = CommentRepository.create_comment(comment_model.to_bson())
        return Comment(**comment_bson)

    @staticmethod
    def get_comments_by_task(task_id: str):
        comments_bson = CommentRepository.get_comments_by_task_id(task_id)
        return [Comment(**c) for c in comments_bson]

    @staticmethod
    def update_comment(comment_id: str, params: UpdateCommentParams) -> Comment:
        updated_comment_bson = CommentRepository.update_comment(comment_id, asdict(params))
        return Comment(**updated_comment_bson)

    @staticmethod
    def delete_comment(comment_id: str) -> None:
        CommentRepository.delete_comment(comment_id)
