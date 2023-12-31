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
    
# Creating a new class Car_Speed to show the current speed of the car.
class Car_Speed:
    # Defining the Car objects
    def __init__(self, root):
        self.root = root
        self.car = Car(2022, 'Toyota')
        self.speed_label = tk.Label(root, text="Current speed: 0")
        self.speed_label.pack()
        self.accelerate_button = tk.Button(root, text="Accelerate", command=self.accelerate)
        self.accelerate_button.pack()
        self.brake_button = tk.Button(root, text="Brake", command=self.brake)
        self.brake_button.pack()

    # Defining the functions of each button of the Gui on showing the Car's current speed
    def update_speed_label(self):
        current_speed = self.car.get_speed()
        self.speed_label.config(text="Current speed: " + str(current_speed))
    
    def accelerate(self):
        self.car.accelerate()
        self.update_speed_label()
    
    def brake(self):
        self.car.brake()
        self.update_speed_label()

# Creating an instance to run the program
if __name__ == "__main__":
    root = tk.Tk()
    car_gui = Car_Speed(root)
    root.mainloop()