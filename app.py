import random
from bs4 import BeautifulSoup
import requests
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def get_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies


def get_movie_info(movie):
    global title
    global year
    global url
    title = movie.a.contents[0]
    year = movie.span.contents[0]
    url = "http://www.imdb.com" + movie.a["href"]
    return title, year, url


def get_user_yn(message):
    while True:
        answer = input(message).upper()
        if answer in ("Y", "N"):
            return answer == "Y"
        print("Invalid input. Please enter a Y or a N. ")


def movie_picker():
    for movie in get_movies("http://www.imdb.com/chart/top"):
        # Parse the movie's url and pull the summary from the details page
        title, year, url = get_movie_info(movie)

        # summary = get_summary(url)

        ########################## BELOW 5 ROWS OF CODE WORKS FOR TERMINAL USAGE OF THE APP ##########################
        # print(title, year)
        # print(url)
        # if not get_user_yn("\nHave you already watched this movie? Enter Y or N. : "):
        #     print("\nEnjoy the movie!")
        #     break
        #############################################################################################################


def generate():
    movie_title_label["text"] = title + " " + year
    movie_url_label.config(text=url)
    movie_url_label.bind("<Button-1>", lambda event: webbrowser.open(url))
    show_popup()


def show_popup():
    result = messagebox.askquestion(
        "Movie Watched", "Have you already watched this movie?", parent=window
    )

    if result == "no":
        information_window = tk.Toplevel(window)
        message_label = Label(
            information_window,
            height=2,
            width=40,
            text="You can click to link above to go to website",
        )
        message_label.pack()
        okay_button = Button(
            information_window,
            text="Okay",
            command=lambda: information_window.destroy(),
        )
        okay_button.pack()

    else:
        movie_title_label["text"] = " "
        movie_url_label["text"] = " "
        movie_picker()


if __name__ == "__main__":
    movie_picker()


# GUI
window = Tk()
window.geometry("1400x400+0+0")
window.title("Random Movie Picker")
font = ("poppins", 14, "bold")

# ADJUSTING BACKGROUND IMAGE SIZE
# Load the image
image = Image.open("bg.jpg")
# Resize the image to fit the window # image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
# Resize the image to fit the window.geometry size
image = image.resize((1400, 400))
# Convert the image to Tkinter-compatible format
image_tk = ImageTk.PhotoImage(image)
# Create a label with the image as the background
bg_label = tk.Label(window, image=image_tk)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# Configure the label to be at the back of all other widgets
bg_label.lower()


top_level = Frame(window, width=780, height=200, bd=2, relief="raise")
top_level.pack(side=TOP, padx=5, pady=5)
mid_level = Frame(window, width=780, height=200, bd=2, relief="raise")
mid_level.pack(side=TOP, padx=5, pady=5)
bottom_level = Frame(window, width=400, height=150, bd=2, relief="raise")
bottom_level.pack(side=TOP, padx=5, pady=5)

movie_title_label = Label(
    top_level, font=font, text="", bd=3, relief="ridge", width=50, justify="center"
)
movie_title_label.grid(row=0, column=0, padx=10, pady=10)
movie_url_label = Label(
    mid_level, font=font, text="", bd=3, width=50, height=1, cursor="hand2"
)
movie_url_label.grid(row=2, column=0, padx=10, pady=10)

generate_button = Button(
    bottom_level,
    bg="wheat",
    pady=1,
    bd=3,
    font=font,
    width=15,
    text="Generate",
    command=generate,
)
generate_button.grid(row=3, column=0, padx=2)

quit_button = Button(
    bottom_level,
    bg="wheat",
    pady=3,
    bd=3,
    font=font,
    width=15,
    text="Quit",
    command=lambda: window.destroy(),
)
quit_button.grid(row=4, column=0, padx=2)

window.mainloop()
