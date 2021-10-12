from flask import Flask, render_template, Markup
import requests

app = Flask(__name__)
@app.route("/", methods=['POST', 'GET'])
def home():
    base_url = "https://zenquotes.io/api/random"
    response = requests.get(base_url)
    raw = response.json()
    quote = Markup(f"{raw[0]['q']} <br/>- {raw[0]['a']}")

    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(threaded=True)