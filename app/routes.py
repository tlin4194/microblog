from flask import render_template
from app import app


@app.route('/index_raw')
def index_raw():
    user = {'username': 'Alice'}
    return f'''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, {user["username"]}! This is a level 1 Header.</h1>
            <h2>This is a level 2 Header.</h2>
            <div><p>This is a paragraph! <b>Some bold text</b></p></div>
        </body>
    </html>'''


@app.route('/')
@app.route('/index')
def index():
    user1 = {'username': 'Alice'}
    user2 = {'username': 'Bob'}
    posts = [
        {
            'author': user1,
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': user2,
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title=user1["username"], user=user1, posts=posts)


@app.route('/index_v2')
def index_v2():
    user1 = {'username': 'Alice'}
    user2 = {'username': 'Bob'}
    posts = [
        {
            'author': user1,
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': user2,
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index2.html', title=user1["username"], user=user1, posts=posts)
