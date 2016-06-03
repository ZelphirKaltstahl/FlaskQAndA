import os
import random

from flask import Flask
app = Flask(__name__)

from flask.views import View
from flask import render_template
from flask import jsonify

from Question import Question
from QuestionsLoader import QuestionsLoader

current_file_directory = os.path.dirname(__file__)

questions_loader = QuestionsLoader()

@app.route("/")
def hello():
	return render_template('index.j2', title='Q & A')

@app.route("/questions/<question_set_identifier>", methods=['GET'])
def get_questions(question_set_identifier):
	return jsonify(questions_loader.get_question_set(question_set_identifier))

if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1', port=5000)
