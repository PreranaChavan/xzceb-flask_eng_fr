from machinetranslation import translator, tests
from flask import Flask, render_template, request
import json
from machinetranslation.translator import english_to_french, french_to_english
"""
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french = english_to_french(textToTranslate)
    return "Translated text to French"+french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english = french_to_english(textToTranslate)
    return "Translated text to English"+english

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def translate_english_to_french():
    english_text = request.form['english_text']
    french_text = english_to_french(english_text)
    return french_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)