from flask import Flask, render_template, request, session, jsonify
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcde1"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def generate_board():
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("nplays", 0)
    nplays = session.get("nplays", 0)

    return render_template('generateBoard.html', board = board, highscore=highscore, nplays=nplays)

# @app.route("/boggle_board", methods = ['GET','POST'])
# def set_up_board():
#     """Sets the Boggle Board."""
    
#     # if 'board' in session:
#     #     board = session['board']
#     # else:
#     #     board = boggle_game.make_board()
#     #     session['board'] = board

#     if request.method == 'POST':
#         guess = request.form.get('guess')
#         session['guess'] = guess
#         result = boggle_game.check_valid_word(board, guess)
#         return render_template('generateBoard.html', board=board, result=result, last_guess=guess)
@app.route("/check-word")
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post_score", methods = ["POST"])
def post_score():

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)
    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord = score > highscore)

if __name__ == "__main__":
    app.run(debug=True)


