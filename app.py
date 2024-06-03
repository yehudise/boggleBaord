from flask import Flask, render_template, redirect
from boggle import Boggle

app = Flask(__name__)

boggle_game = Boggle()


@app.route("/boggle_board", methods = ['GET','POST'])
def set_up_baord():
    """Sets the Boggle Board."""
    board = boggle_game.make_board()
    return render_template('generateBoard.html', board = board)

    

ç




