from flask import jsonify, request, g, url_for, session
from flask_login import current_user
from .. import db
from app.models import Post, Permission
from . import api
from .errors import forbidden


# @bp.before_request
# def before_request():
#     g.user = current_user


@api.route('/posts/')
def get_posts():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.paginate(
        page, per_page=10,
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page + 1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/posts/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())


# @bp.route('/posts/', methods=['POST'])
# def new_post():
#     if  session.new:
#         return forbidden('Insufficient permissions')

#     else:
#         post = Post.from_json(request.json)
#         post.author = g.current_user
#         db.session.add(post)
#         db.session.commit()
#         return jsonify(post.to_json()), 201, \
#             {'Location': url_for('api.get_post', id=post.id)}


# @bp.route('/posts/<int:id>', methods=['PUT'])
# def edit_post(id):
#     post = Post.query.get_or_404(id)
#     if g.current_user != post.author and \
#             not g.current_user.can(Permission.ADMIN):
#         return forbidden('Insufficient permissions')
#     post.body = request.json.get('body', post.body)
#     db.session.add(post)
#     db.session.commit()
#     return jsonify(post.to_json())
