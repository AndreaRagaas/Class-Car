# Importing Tkinter to add a Gui for the current speed of the Car
import tkinter as tk

# Creating the class Car
class Car:
    # Defining all of the objects for the Car
    def __init__(self, year_model, make):
        self._year_model = year_model
        self._make = make
        self._speed = 0
    
    def accelerate(self):
        self._speed += 5
        print("Accelerating. Current speed:", self._speed)
    
    def brake(self):
        self._speed -= 5
        print("Braking. Current speed:", self._speed)
    
    def get_speed(self):
        return self._speed