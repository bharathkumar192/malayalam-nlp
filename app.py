import os
from flask import Flask, render_template, request,url_for
from flask.helpers import send_from_directory
import requests
# from urllib.parse import quote
import json
from malayalam.__init__ import splitter
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from SpellCheck import load1stCluster, loadLastCluster, loadcharIndex, readForwardFSA, readReverseFSA, loadTrigramFreqHash, loadTrigramOpt, loadCiC, spellchk, split_chars,suggestionGeneration


load1stCluster()
loadLastCluster()
loadcharIndex()
readForwardFSA()
readReverseFSA()
loadTrigramFreqHash()
loadTrigramOpt()
loadCiC()


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        mal_word = request.form["English Text"]
    final = splitter().split(mal_word)
    print(final)
    return render_template('index.html',init_word = mal_word, Split = final )


@app.route('/spellcheck', methods=['GET', 'POST'])
def spell():
    if request.method == 'POST':
        mal_word = request.form["English Text"]
    errorWords = []
    if mal_word:
        for word in mal_word.split(' '):
            if spellchk(word) == 0:
                errorWords.append(word)
   
    return render_template('index.html',spell_word = mal_word, Spell = errorWords )


@app.route('/suggestor', methods=['GET', 'POST'])
def suggest():
    if request.method == 'POST':
        mal_word = request.form["English Text"]
    suggestions = []
    if mal_word:
        if spellchk(mal_word) == 0:
            suggestions = suggestionGeneration(split_chars(mal_word))

    return render_template('index.html',sugg_word = mal_word, Suggest = suggestions )




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/x-icon')





if __name__ == '__main__':
    app.run(debug=True)
