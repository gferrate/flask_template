from words import words
from flask import Flask, render_template, jsonify, redirect, request, \
    session, send_from_directory

import datetime

app = Flask(__name__)


@app.route('/')
def index():
    title = 'This is a blank example with random words'
    return render_template('index.html', title=title, words=words)


@app.route('/<word>/')
def word(word):
    title = 'WOW! Really cool word: '
    return render_template('word.html', title=title, word=word)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
