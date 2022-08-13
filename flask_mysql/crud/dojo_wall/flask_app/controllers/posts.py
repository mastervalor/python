from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.post import Posts
from flask_app.models.user import Users
from flask_app.models.comment import Comments

@app.route('/posts')
def posts():
    if 'user_id' not in session:
        return redirect('/')
    user = {
        "id": session['user_id']
    }
    return render_template('posts.html', posts=Posts.get_all_posts(), user=Users.get_by_id(user), comments=Comments.get_comments_by_post())

@app.route('/post/create', methods=['POST'])
def publish_post():
    if not request.form['content']:
        flash("* Post conetnt must not be blank", 'posts')
        return redirect('/posts')
    data = {
        "content": request.form['content'],
        "user_id": session['user_id']
    }
    Posts.create_post(data)
    return redirect('/posts')

@app.route('/delete/<int:id>')
def destroy_post(id):
    data = {
        "id": id
    }
    Posts.delete_post(data)
    return redirect("/posts")