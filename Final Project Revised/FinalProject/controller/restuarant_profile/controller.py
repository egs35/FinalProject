from finalproject.models.restaurants import restaurant

def create_restaurant_profile(name, rating, review, price, location):
    return restaurant(name, rating, review, price, location)