from flask import render_template
from .action import create_restaurant_profile

def profile_view():
    pet = create_pet_profile("stack'd", 5 , "great burgers!" , $$ , Oakland)
    return render_template("profile.html", pet=pet)