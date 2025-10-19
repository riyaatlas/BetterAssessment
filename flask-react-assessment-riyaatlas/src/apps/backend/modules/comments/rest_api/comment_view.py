from flask.views import MethodView
from flask import request, jsonify
from modules.comments.types import CreateCommentParams, UpdateCommentParams
from modules.comments.internals.comment_service import CommentService

class CommentView(MethodView):
    def post(self):
        data = request.get_json()
        params = CreateCommentParams(**data)
        comment = CommentService.create_comment(params)
        return jsonify(comment.__dict__), 201

    def get(self, task_id):
        comments = CommentService.get_comments_by_task(task_id)
        return jsonify([c.__dict__ for c in comments]), 200

    def patch(self, comment_id):
        data = request.get_json()
        params = UpdateCommentParams(**data)
        comment = CommentService.update_comment(comment_id, params)
        return jsonify(comment.__dict__), 200

    def delete(self, comment_id):
        CommentService.delete_comment(comment_id)
        return "", 204
