from flask import Flask, render_template, Markup
import random

app = Flask(__name__)
@app.route("/")
def home():
    quotes = [
    'You are the shuckiest shuck faced shuck in the world!',
    'Insane means fewer cameras!',
    "I'm about as intimidating as a butterfly.",
    'Act first, explain later.'
]

    random_quotes = random.choice(quotes)
    return render_template('index.html', quote=random_quotes)

if __name__ == '__main__':
    app.run(threaded=True)