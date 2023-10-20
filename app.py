#importing requisite libraries
from flask import Flask, render_template,request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort

#initialising flask components
app = Flask(__name__)
app.config['SECRET_KEY'] = 'moonlightchickenismyfavourite'

#connection for the db
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#inserting values in db and extracting it using ID number
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

#sql code to display all the posts
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
#render the post ID numbers
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

#code to render the about page
@app.route('/about')
def aboutpage():
    return render_template('about.html')

#code to create a blogpost from the website
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

#edit the blogpost
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

#delete the blogpost
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

#render the firstblog
@app.route('/firstblog')
def firstpage():
    return render_template('firstblog.html')

@app.route('/contactme')
def contactme():
    return render_template('contactme.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

#render the second blog
@app.route('/secondblog')
def secondpage():
    return render_template('secondblog.html')

@app.route('/thirdblog')
def seconddayoflearning():
    return render_template('thirdblog.html')

@app.route('/fourthblog')
def thirddayoflearning():
    return render_template('fourthblog.html')

@app.route('/fifthblog')
def fourthdayoflearning():
    return render_template('fifthblog.html')

@app.route('/sixthblog')
def fifthdayoflearning():
    return render_template('sixthblog.html')

@app.route('/seventhblog')
def sixthdayoflearning():
    return render_template('seventhblog.html')

@app.route('/eighthblog')
def seventhday():
    return render_template('eighthblog.html')

@app.route('/ninethblog')
def eigthday():
    return render_template('ninethblog.html')

@app.route('/tenthblog')
def ninethday():
    return render_template('tenthblog.html')

@app.route('/11thblog')
def tenthday():
    return render_template('11blog.html')

@app.route('/12thblog')
def eleventhday():
    return render_template('12blog.html')

@app.route('/13thblog')
def twelthday():
    return render_template('13blog.html')

@app.route('/14thblog')
def thirteenthday():
    return render_template('14blog.html')

@app.route('/15thblog')
def fourtheenthday():
    return render_template('15blog.html')

@app.route('/16thblog')
def fifteenthday():
    return render_template('16blog.html')


#direction to projects
@app.route('/brainstrokeprediction')
def project1():
    return render_template('brainstroke.html')

@app.route('/cryptoprediction')
def project2():
    return render_template('cryptoprediction.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    