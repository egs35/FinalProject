from flask import render_template


def restaurant_view():
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