'''
Lesson 04
code - url_for
'''

import os
from flask import Flask, render_template, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

menu=["Установка", "Первое приложение", "Обратная связь"]

@app.route('/')
def index():
    print(url_for("index"))
    return render_template('index.html', menu=menu)

@app.route('/about')
def about():
    print(url_for("about"))
    return render_template('about.html', title="О сайте", menu=menu)

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