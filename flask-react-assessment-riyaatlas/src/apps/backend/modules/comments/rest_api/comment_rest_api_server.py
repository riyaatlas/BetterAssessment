from flask import Blueprint
from modules.comments.rest_api.comment_router import CommentRouter


class CommentRestApiServer:
    @staticmethod
    def create() -> Blueprint:
        comment_api_blueprint = Blueprint("comments", __name__)
        return CommentRouter.create_route(blueprint=comment_api_blueprint)
