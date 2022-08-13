from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.post import Posts
from flask_app.models.user import Users
from flask_app.models.comment import Comments

@app.route('/comment/create', methods=['POST'])
def publish_comment():
    if not request.form['content']:
        flash("* comment conetnt must not be blank", 'comment')
        return redirect('/posts')
    data = {
        "content": request.form['content'],
        "post_id": request.form['post_id'],
        "commenter_id": session['user_id']
    }
    Comments.create_comment(data)
    return redirect('/posts')

@app.route('/delete/comment/<int:id>')
def destroy_comment(id):
    data = {
        "id": id
    }
    Comments.delete_comment(data)
    return redirect("/posts")