from random import randint
from tkinter import *
from tkinter import messagebox
import json

def generate_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

def search():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= website , message= "no such website on the file")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email : {email} \n Password {password}")
        else:
            messagebox.showinfo(title=website, message="data has not been added yet")
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website:  {"email" : email, "password": password}}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Fill all the blanks")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n {email} | {password}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)


window = Tk()
window.title("Password manager")
window.config(pady="100", padx="100", bg="skyblue")

canvas = Canvas(width=300, height=224, bg="skyblue", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=logo_img)
canvas.grid(column=1, row=1)
website_text = Label(text="Website:", bg="skyblue")
website_text.grid(column=0, row=3)
website_input = Entry(width=35)
website_input.grid(column=1, row=3, columnspan=2)
website_input.focus()
email_text = Label(text="Email/Username:", bg="skyblue")
email_text.grid(column=0, row=4)
email_input = Entry(width=35)
email_input.grid(column=1, row=4, columnspan=2)
password_text = Label(text="Password:", bg="skyblue")
password_text.grid(column=0, row=5)
password_input = Entry(width=35)
password_input.grid(column=1, row=5, columnspan=2)
search_button = Button(text="search", command = search)
search_button.grid(column=2, row=3)
password_button = Button(text="Generate password", command= generate_pass)
password_button.grid(column=3, row=5)
add_info = Button(text="Add", width=30, command=save)
add_info.grid(column=1, row=7, columnspan=2)

window.mainloop()
