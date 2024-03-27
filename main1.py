import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurants")  
    '''
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            rating TEXT,
            review TEXT,
            price TEXT,
            location TEXT
        )
    '''
    conn.commit()
    conn.close()

# Function to add a new restaurant to the database
def add_restaurant(name, rating, review, price, location):
    name = input("Enter the name of the restaurant: ")
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
    location = input("Enter the location of the restaurant: ")

    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO restaurants (name, rating, review, price, location)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, rating, review, price, location))
    conn.commit()
    conn.close()

# Call initialize_database function
initialize_database()

#while True:
#    response= input("Do you want to add a new restaurant?"). lower()

#    if response == 'yes':
#        add_restaurant
#      print("Exiting...")
#        break 
#    else:
#        print("invalid input. Please enter 'yes' or 'no'.")
        

# Example usage:
# Add some restaurants
add_restaurant('name','rating','review','price','location')

# # Function to remove a restaurant from the database by name
# def remove_restaurant_by_name(name):
#     conn = sqlite3.connect('restaurants.db')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM restaurants WHERE name = ?', (name,))
#     conn.commit()
#     conn.close()

# # # Example usage:
# remove_restaurant_by_name("Stackd")
# remove_restaurant_by_name("Mount Everest Sushi")

# Retrieve and print all restaurants
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM restaurants')
restaurants = cursor.fetchall()

# Convert each tuple row to a list and store in a new list
rows_as_lists = [list(restaurant) for restaurant in restaurants]

# Now rows_as_lists contains each row as a separate list
#for row_list in rows_as_lists:
   # print(row_list)

conn.close()

# for restaurant in restaurants:
#     print("Name:", restaurant[1])
#     print("Rating:", restaurant[2])
#     print("Review:", restaurant[3])
#     print("Price Range:", restaurant[4])
#     print("Location:", restaurant[5])
#     print()


# Dictionary to combine restaurants
combined_restaurants = {}

for restaurant in restaurants:
    name, rating, review, price, location = restaurant[1:]
    if name in combined_restaurants:
        # Update existing restaurant entry
        combined_restaurants[name]['ratings']+= ';' + rating
        if review not in combined_restaurants[name]['reviews']:
            combined_restaurants[name]['reviews'] += ';' + review
        if price not in combined_restaurants[name]['prices']:
            combined_restaurants[name]['prices'] += ';' + price
        if location not in combined_restaurants[name]['locations']:
            combined_restaurants[name]['locations'] += ';' + location
    else:
        # Create new restaurant entry
        combined_restaurants[name] = {
            'ratings': rating,
            'reviews': review,
            'prices': price,
            'locations': location
        }

# Process combined data
for name, data in combined_restaurants.items():
    print(f"{name}: Ratings: {data['ratings']}, Reviews: {data['reviews']}, Prices: {data['prices']}, Locations: {data['locations']}")
    print()
