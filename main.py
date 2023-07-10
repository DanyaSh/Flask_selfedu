'''
--------------------------Lessons Flask form youtube chanel selfedu--------------------------
'''
about= "Lesson 09"
code_name= "add_post"
'''
🔻 Introduction:
    List-----------------------------------------------------------------------------------
        ✅ SQLite
        ⚪️ Add post
        🔴 app.config.from_object(env) (line 29)
        🔵 Lesson 09 stop on 06:00
    Legend-----------------------------------------------------------------------------------
        ✅ Done
        ⚪️ Plan
        ⚫️ Low
        🔵 Medium
        🔴 High
        ❗️ Critical
'''

import os
import sqlite3
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from dotenv import load_dotenv
from FDataBase import FDataBase

env=load_dotenv('.env')

app = Flask(__name__)
app.config.from_object(env) #❗️This line doesn't work
app.config.update(dict(DATA_BASE=os.path.join(app.root_path, 'site.db')))

def connect_db():
    conn=sqlite3.connect(app.config['DATA_BASE'])
    conn.row_factory=sqlite3.Row
    return conn

def create_db():
    print(app.config['DATA_BASE'])
    db=connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db=connect_db()
    return g.link_db

@app.route('/')
def index():
    print(url_for("index"))
    db=get_db()
    dbase=FDataBase(db)
    menu=dbase.get_menu()
    return render_template('index.html', menu=dbase.get_menu())

@app.route('/about')
def about():
    print(url_for("about"))
    db=get_db()
    dbase=FDataBase(db)
    menu=dbase.get_menu()
    return render_template('about.html', title="О сайте", menu=dbase.get_menu())

@app.route('/login', methods=["POST", "GET"])
def login():
    print(url_for("login"))
    db=get_db()
    dbase=FDataBase(db)
    menu=dbase.get_menu()
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method=="POST" and request.form['username']=='danyash' and request.form['pswd']=='123':
        session['userLogged']=request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=dbase.get_menu())

@app.route('/contact', methods=["POST", "GET"])
def contact():
    print(url_for('contact'))
    db=get_db()
    dbase=FDataBase(db)
    menu=dbase.get_menu()
    if request.method=="POST":
        if len(request.form['username'])>2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title="Обратная связь", menu=menu)

@app.route('/profile/<path:username>')
def profile(username):
    print(url_for("profile", username=username))
    db=get_db()
    dbase=FDataBase(db)
    menu=dbase.get_menu()
    if 'userLogged' not in session or session['userLogged']!=username:
        abort(401)
    return f"Пользователь: {username}"

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        print('close connection data base')
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu()), 404

# with app.test_request_context():
#     print(url_for("index"))

# with app.test_request_context():
#     print(url_for("about"))

if __name__=="__main__":
    app.run(debug=True)