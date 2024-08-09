from tkinter import *
from PIL import Image, ImageTk
import csv
import time

# Initialize tkinter window
win = Tk()
win.title('Greeting')
win.geometry('800x600')
win.config(bg='black')

# Global variable to store orders
orders = []

# Check variables
checkvars = [IntVar() for _ in range(8)]


def button_click():
    global orders
    # Get name from entry box
    name = name_entry.get()

    # Reset orders list
    orders = []

    # Check which items are selected and add them to orders list
    selected_items = [items[i] for i, var in enumerate(checkvars) if var.get()]
    orders.extend(selected_items)

    # Calculate total cost
    total_cost = len(orders) * 5.5

    # Display name and total cost
    result_label.config(text=f"Thank you {name}, Total cost is ${total_cost:.2f}")

    # Write to csv file
    with open('orders.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, time.strftime('%c'), ', '.join(orders), f"{total_cost:.2f}"])

    # Clear checkboxes
    clear_checkboxes()


def clear_checkboxes():
    for var in checkvars:
        var.set(0)


def close():
    win.destroy()


# Frame to hold the content
frame = Frame(win, bg='black')
frame.pack(expand=True, fill=BOTH, padx=50, pady=50)

# Canvas and image
logo = Image.open('bottle.jpg')
logo.thumbnail((300, 150))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(frame, image=logo, bg='black')
logo_label.pack(pady=20)

# Labels
greeting_label = Label(frame, text="Welcome to Bottle Coffee", fg='white', bg='black', font=("Arial", 16))
greeting_label.pack(pady=10)

price_label = Label(frame, text="Order Form *Every item is $5.50", fg='white', bg='black', font=("Arial", 12))
price_label.pack(pady=10)

name_label = Label(frame, text="Enter your name:", fg='white', bg='black', font=("Arial", 12))
name_label.pack(pady=10)

# Entry box
name_entry = Entry(frame, justify=CENTER, font=("Arial", 12))
name_entry.pack(pady=10)

# Checkboxes
items = ["Iced Mint Mojito", "Iced Black", "Bottle Burger", "Bottle Ice Cream", "Iced Samatra", "Hot Black",
         "Bottle Fries", "Bottle Muffin"]

checkbox_frame = Frame(frame, bg='white')
checkbox_frame.pack(pady=10)

for i, item in enumerate(items):
    col = i % 4
    row = i // 4
    Checkbutton(checkbox_frame, text=item, variable=checkvars[i], font=("Arial", 12), bg='white', fg='black').grid(
        row=row, column=col, padx=10, pady=5)

# Button frame
button_frame = Frame(frame, bg='black')
button_frame.pack(pady=20)

# Submit button
submit_button = Button(button_frame, text="Submit", font=("Arial", 16), command=button_click)
submit_button.pack(side=LEFT, padx=10)

# Exit button
exit_button = Button(button_frame, text="Exit", font=("Arial", 16), command=close)
exit_button.pack(side=LEFT, padx=10)

# Result label
result_label = Label(frame, text="", font=("Arial", 12), fg='white', bg='black')
result_label.pack(pady=20)

win.mainloop()













