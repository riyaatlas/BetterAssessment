from flask import Blueprint
from .comment_view import CommentView

class CommentRouter:
    @staticmethod
    def create_route():
        blueprint = Blueprint("comments", __name__)
        blueprint.add_url_rule("/comments", view_func=CommentView.as_view("create_comment"), methods=["POST"])
        blueprint.add_url_rule("/comments/task/<task_id>", view_func=CommentView.as_view("get_comments"), methods=["GET"])
        blueprint.add_url_rule("/comments/<comment_id>", view_func=CommentView.as_view("update_comment"), methods=["PATCH"])
        blueprint.add_url_rule("/comments/<comment_id>", view_func=CommentView.as_view("delete_comment"), methods=["DELETE"])
        return blueprint
