import db_layer
from tkinter import *

def display_text():
    get_text = db_layer.main().getFanDetailsFromDB(int(fan_id_entry.get()))
    if listing_window.get("1.0", "end-1c") != "":
        listing_window.delete("1.0", END)
    listing_window.insert(END, f"{get_text}\n")

root = Tk()
root.title("Ticket Management System")

# creating main label
main_label = Label(root, text="Ticket Management System", font=("Helvetica", 16))
main_label.grid(row=0, column=1, pady=10)

# listing the values
listing_window = Text(root, height=10, width=40, padx=10)
listing_window.grid(row=1, column=1, pady=10)
listing_window.insert("1.0", "No text to display at the moment...")



# creating a label for fan_id
fan_id_label = Label(root, text="Enter Fan ID: ", font=("sans-serif", 10))
fan_id_label.grid(row=8, column=0)

# creating entry for fan_id
fan_id_entry = Entry(root, width=50, borderwidth=2)
fan_id_entry.grid(row=8, column=1)

# Create a Button for fan_id display
button = Button(root, text="Get Details", command=display_text)
button.grid(row=8, column=3)








root.geometry("1100x600")
root.mainloop()

