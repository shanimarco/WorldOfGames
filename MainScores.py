import os
import signal
from flask import Flask, jsonify
from flask import render_template

app = Flask("game")

# @app.route('/shutdown', methods=['POST'])
# def shutdown():
#    print("Shutting down gracefully...")
#    os.kill(os.getpid(), signal.SIGINT)
#    return 'Server shutting down...'


@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })


@app.route('/worldOfGame', methods=['GET'])
def score_server():
        try:
                with open("Score.txt", 'r') as my_file:
                        score = my_file.read()
                        my_file.close()
                        return render_template('success.html', SCORE=score)
        except FileNotFoundError as ve:
                return render_template('error.html', ERROR=ve)

app.run(host="0.0.0.0", port=5001, debug=True)