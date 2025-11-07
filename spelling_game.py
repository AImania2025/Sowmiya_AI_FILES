from flask import Flask
from flask import Flask, request, session, redirect, url_for

import random

app = Flask(__name__)
app.secret_key = "spelling_secret_key"

# --- Word list (word + definition) ---
WORDS = [
    ("accomplish", "To succeed in doing something; to complete successfully."),
    ("beautiful", "Pleasing the senses or mind aesthetically."),
    ("curiosity", "A strong desire to learn or know something."),
    ("delicious", "Highly pleasant to the taste."),
    ("elephant", "A very large gray mammal with a trunk.")
]

# --- Home route ---
@app.route("/")
def home():
    return (
        "🎯 Welcome to the Flask Spelling Game!<br>"
        "Type /start in the address bar to begin the game.<br>"
        "Example: http://127.0.0.1:5000/start"
    )

# --- Start new game ---
@app.route("/start")
def start():
    random.shuffle(WORDS)
    session["index"] = 0
    session["score"] = 0
    return redirect(url_for("question"))

# --- Ask question ---
@app.route("/question")
def question():
    if "index" not in session:
        return redirect(url_for("start"))

    index = session["index"]

    if index >= len(WORDS):
        return redirect(url_for("result"))

    definition = WORDS[index][1]
    return (
        f"🧩 Definition: {definition}<br>"
        f"👉 Type your answer like this:<br>"
        f"/answer?word=your_guess_here"
    )

# --- Check answer ---
@app.route("/answer")
def answer():
    if "index" not in session:
        return redirect(url_for("start"))

    user_word = request.args.get("word", "").strip().lower()
    index = session["index"]

    if index >= len(WORDS):
        return redirect(url_for("result"))

    correct_word = WORDS[index][0].lower()

    if user_word == correct_word:
        session["score"] += 1
        response = "✅ Correct!"
    else:
        response = f"❌ Wrong! Correct spelling was: {correct_word}"

    session["index"] = index + 1

    if session["index"] < len(WORDS):
        next_url = url_for("question")
        return f"{response}<br><br><a href='{next_url}'>Next Word</a>"
    else:
        return redirect(url_for("result"))

# --- Final score ---
@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(WORDS)
    return (
        f"🏁 Game Over!<br>"
        f"Your score: {score}/{total}<br><br>"
        f"<a href='/start'>Play Again</a>"
    )

if __name__ == "__main__":
    app.run(debug=True)
