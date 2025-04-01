from flask import Flask, render_template
from flask_socketio import SocketIO
from game import Gomoku

app = Flask(__name__)
socketio = SocketIO(app)
game = Gomoku()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('make_move')
def handle_move(data):
    row, col = data['row'], data['col']
    if game.make_move(row, col):
        socketio.emit('update_board', {'board': game.board, 'currentPlayer': game.current_player})
        if game.check_win(row, col):
            socketio.emit('game_over', {'winner': game.current_player})
            game.reset()

if __name__ == '__main__':
    socketio.run(app, debug=True)
