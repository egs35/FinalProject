import sqlite3

from flask import Flask, render_template, g
from model.restaurants import Restaurant


app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("restaurants.db")
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/restaurants")
def restaurants():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurants")
    restaurants = cursor.fetchall()
    res_obj = []
    for restaurant in restaurants:
        res_obj.append(
            Restaurant(
                name=restaurant[1],
                rating=restaurant[2],
                review=restaurant[3],
                price=restaurant[4],
                location=restaurant[5],
            )
        )
    return render_template("restaurants.html", restaurants=res_obj)


@app.route('/restaurants_reviews/<name>')
def restaurant_review_view(name):
    pass
#     return restaurants_reviews_view()

# @app.route('/add')
# def add():
#     return add_view()

if __name__ == "__main__":
    app.run(debug=True)
