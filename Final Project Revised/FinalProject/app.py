import sqlite3

from flask import Flask, render_template, g, request
from model.restaurants import Restaurant
from model.restaurants_reviews import RestaurantReview
from main1 import load_reviews_from_csv

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


@app.route('/restaurants_reviews')
def restaurants_reviews():
    restaurants = load_reviews_from_csv("reviews.csv")
    print(restaurants)
    res_review_obj = []
    for restaurants_reviews in restaurants:
        if restaurants_reviews["restaurant"] == request.args.get("name"):
            res_review_obj.append(
                RestaurantReview(
                    restaurant=None,
                    name=restaurants_reviews["restaurant"],
                    rating=restaurants_reviews["rating"],
                    review_text=restaurants_reviews["review_text"],
                    reviewer=restaurants_reviews["reviewer"],
                )
            )
    return render_template("restaurants_reviews.html", restaurants_reviews=res_review_obj)

    
   

#     return restaurants_reviews_view()

# @app.route('/add')
# def add():
#     return add_view()

if __name__ == "__main__":
    app.run(debug=True)
