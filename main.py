
# main.py
from flask import Flask, render_template, request, redirect, url_for
import nltk

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vocabulary = request.form.get("vocabulary")
        sentence = request.form.get("sentence")

        # AI-powered NLP module for critique generation
        critiques = nltk.pos_tag(nltk.word_tokenize(sentence))

        return render_template('results.html', vocabulary=vocabulary, sentence=sentence, critiques=critiques)
    return render_template('index.html')

@app.route('/results', methods=["GET"])
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
