from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)
DB_NAME = "tree_tracker_ai.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS plantations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tree_name TEXT NOT NULL,
        location TEXT NOT NULL,
        count INTEGER NOT NULL,
        date TEXT NOT NULL,
        watering_per_week INTEGER NOT NULL,
        season TEXT NOT NULL,
        predicted_survival REAL NOT NULL,
        actual_survival REAL
    )
    """)
    conn.commit()
    conn.close()


def season_from_month(date_str):
    month = int(date_str.split("-")[1])
    if month in [6, 7, 8, 9]:
        return "Monsoon"
    elif month in [3, 4, 5]:
        return "Summer"
    else:
        return "Winter"


def encode_season(season):
    return {"Summer": 0, "Winter": 1, "Monsoon": 2}.get(season, 1)


def train_model():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query(
        "SELECT count, watering_per_week, season, actual_survival FROM plantations WHERE actual_survival IS NOT NULL",
        conn
    )
    conn.close()

    if len(df) < 5:
        return None

    df["season_code"] = df["season"].apply(encode_season)

    X = df[["count", "watering_per_week", "season_code"]]
    y = df["actual_survival"]

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X, y)
    return model


def fallback_prediction(count, watering, season):
    base = 70

    if season == "Monsoon":
        base += 15
    elif season == "Summer":
        base -= 15

    if watering >= 4:
        base += 10
    elif watering <= 2:
        base -= 10

    if count < 5:
        base -= 5
    elif count > 20:
        base += 5

    return max(10, min(95, base))


def predict_survival(count, watering, season):
    model = train_model()
    if model is None:
        return fallback_prediction(count, watering, season)

    season_code = encode_season(season)
    pred = model.predict([[count, watering, season_code]])[0]
    return max(10, min(95, float(pred)))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tree_name = request.form["tree_name"]
        location = request.form["location"]
        count = int(request.form["count"])
        watering = int(request.form["watering"])

        date_str = request.form["date"]
        if not date_str:
            date_str = datetime.today().strftime("%Y-%m-%d")

        season = season_from_month(date_str)
        predicted_survival = predict_survival(count, watering, season)

        actual_survival = request.form.get("actual_survival")
        actual_survival = float(actual_survival) if actual_survival else None

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO plantations
            (tree_name, location, count, date, watering_per_week, season, predicted_survival, actual_survival)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (tree_name, location, count, date_str, watering, season, predicted_survival, actual_survival))
        conn.commit()
        conn.close()

        return render_template(
            "index.html",
            success=True,
            predicted_survival=predicted_survival,
            season=season
        )

    return render_template("index.html", success=False)


@app.route("/records")
def records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM plantations ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()

    return render_template("records.html", rows=rows)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, use_reloader=False)
