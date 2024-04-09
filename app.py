import sqlite3
from flask import Flask

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/restaurants')
def restaurants():
    return restaurants_view()

@app.route('/add')
def add():
    return add_view()

if __name__ == '__main__':
    app.run(debug=True)