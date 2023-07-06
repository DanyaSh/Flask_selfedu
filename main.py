'''
Lesson 06
code - flash
'''

import os
from flask import Flask, render_template, url_for, request, flash
from dotenv import load_dotenv

load_dotenv('.env')

app = Flask(__name__)
app.config['DATA_TEXT'] = os.getenv('DATA_TEXT')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

menu=[{'name':"Установка", 'url':'install-flask'},
      {'name':"Первое приложение", 'url':'first-app'},
      {'name':os.getenv('DATA_TEXT'), 'url':'contact'}]

@app.route('/')
def index():
    print(url_for("index"))
    return render_template('index.html', menu=menu)

@app.route('/about')
def about():
    print(url_for("about"))
    return render_template('about.html', title="О сайте", menu=menu)

@app.route('/contact', methods=["POST", "GET"])
def contact():
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
    return f"Пользователь: {username}"

# with app.test_request_context():
#     print(url_for("index"))

# with app.test_request_context():
#     print(url_for("about"))

if __name__=="__main__":
    app.run(debug=True)