class Restaurant: 
    def __init__(self, name, rating, review, price, location):
        self.name = name
        self.rating = rating 
        self.review = review 
        self.price = price
        self.location = location

    def add_restaurant(name, rating, review, price, location):
        name = input("Enter the name of the restaurant: ").lower()
        rating_str = input("Enter the rating of the restaurant out of 5 stars: ")
        try:
            rating = int(rating_str)
        except ValueError:
            print("Invalid input for rating. Please enter a number.")
            # Handle the error, maybe ask for input again or provide a default value
            rating = None  # You may want to provide a default rating here
        review = input("Enter a review for the restaurant: ")
        while True:
            price = input("Enter the price range of the restaurant ($, $$, $$$): ")
            if price in ['$', '$$', '$$$']:
                break
            else:
                print("invalid price range. Please enter $, $$, or $$$.")
        location = input("Enter the location of the restaurant: ").lower()

    def edit_rating(self, rating1):
        self.rating1 = rating1