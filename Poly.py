import tkinter as tk 

class Animal:
    def make_sound(self):
        return "Some sound"

class Bird(Animal):
    def make_sound(self):
        return "Tweet tweet"

class Dog(Animal):
    def make_sound(self):
        return "Woof Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meong Meong"

class Cow(Animal):
    def make_sound(self):
        return "Moo Moo"

def show_sound(animal):
    label_result.config(text=animal.make_sound())

root = tk.Tk()
root.title("Polimorfisme di Tkinter")

label_result = tk.Label(root, text="Klik salah satu tombol untuk mendegar suara hewan,", font=("Arial", 14))
label_result.pack(pady=20)

button_bird = tk.Button(root, text="Burung", font=("Arial", 12), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)

button_dog = tk.Button(root, text="Anjing", font=("Arial", 12), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

button_cat = tk.Button(root, text="Kucing", font=("Arial", 12), command=lambda: show_sound(Cat()))
button_cat.pack(pady=10)

button_cow = tk.Button(root, text="Sapi", font=("Arial", 12), command=lambda: show_sound(Cow()))
button_cow.pack(pady=10)

button_animal = tk.Button(root, text="Hewan Umum", font=("Arial", 12), command=lambda: show_sound(Animal()))
button_animal.pack(pady=10)

root.mainloop()

