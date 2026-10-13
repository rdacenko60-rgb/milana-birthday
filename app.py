from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

HER_NAME = "Милана"
NICKNAME = "Конфетка"
AGE = 14
BIRTHDAY = date(2026, 11, 1)
GAME_SCORE_TO_WIN = 15

@app.route("/")
def index():
    today = date.today()
    days_left = (BIRTHDAY - today).days
    return render_template(
        "index.html",
        name=HER_NAME,
        nickname=NICKNAME,
        age=AGE,
        days_left=days_left,
        is_birthday=(days_left == 0),
        win_score=GAME_SCORE_TO_WIN
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
