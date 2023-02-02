from flask import Flask, render_template, request

import forms
from config import Config
from game import Game

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/intro/')
def intro():
    form = forms.UserNameForm()
    return render_template('intro.html', game=Game(), form=form)


@app.route('/game/<current>', methods=['POST', 'GET'])
def game(current):
    form = forms.GameForm()

    if request.method == "POST":
        current_position = [int(x) for x in current.split('-')]

        if request.form.get('user_name'):
            user_name = request.form.get('user_name')

        current_game = Game(current_position, user_name)

        if request.form.get('stages'):
            current_game.move(current_position, request.form.get('direction'),
                              int(request.form.get('stages')))
        return render_template('game.html', form=form, game=current_game)
    else:
        return render_template('game.html', form=form, game=Game())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
