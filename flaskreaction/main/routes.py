from flask import Blueprint, render_template, request
from flaskreaction.models import Post

main = Blueprint('main',__name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', title='Blag', posts=posts)

@main.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')
