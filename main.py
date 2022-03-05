import requests
from tkinter import *
from tkinter import messagebox


def connect2api():
    user_input1 = movie_input.get()
    url = f"https://www.omdbapi.com/?apikey=79ae1bdd&t={user_input1.lower()}"
    # passing url to get information about movie
    response = requests.get(url)

    # Get json data from URL
    json_data = response.json()
    year = json_data['Year']
    year_input_label.insert(0, year)
    actors = json_data['Actors']
    actors_input_label.insert(0, actors)
    genre = json_data['Genre']
    genre_input_label.insert(0, genre)
    director = json_data['Director']
    director_input_label.insert(0, director)
    lang = json_data['Language']
    language_input_label.insert(0, lang)
    IMDB = json_data['imdbRating']
    imdb_input.insert(0, IMDB)


def movie_details():
    user_input = movie_input.get()

    if len(user_input) == 0:
        messagebox.showwarning(title="No movie entered", message="Please enter movie name")
    else:
        connect2api()


def clear_button():
    movie_input.delete(0, END)
    year_input_label.delete(0, END)
    actors_input_label.delete(0, END)
    language_input_label.delete(0, END)
    imdb_input.delete(0, END)
    director_input_label.delete(0, END)
    genre_input_label.delete(0, END)
    movie_input.focus()


# --------------------------------------------- Creating GUI from Tkinter--------------------------------------
window = Tk()
window.title("Movie Information Database")
window.config(padx=50, pady=100)

canvas = Canvas()
movie_logo = PhotoImage(file="movie.png")
canvas.create_image(150, 100, image=movie_logo)
canvas.grid(column=1, row=0)

input_label = Label()
input_label = Label(text="Enter Movie Name:", font=('Arial', 12, 'bold'))
input_label.grid(row=1, column=0)

movie_input = Entry(width=35)
movie_input.grid(row=1, column=1)
movie_input.focus()

year_label = Label(text="Release Year:", font=('Arial', 12, 'bold'))
year_label.grid(row=2, column=0)

year_input_label = Entry(width=35)
year_input_label.grid(row=2, column=1)

actors_label = Label(text="Actors:", font=('Arial', 12, 'bold'))
actors_label.grid(row=3, column=0)

actors_input_label = Entry(width=35)
actors_input_label.grid(row=3, column=1)

genre_label = Label(text="Genre:", font=('Arial', 12, 'bold'))
genre_label.grid(row=4, column=0)

genre_input_label = Entry(width=35)
genre_input_label.grid(row=4, column=1)

director_label = Label(text="Directed By:", font=('Arial', 12, 'bold'))
director_label.grid(row=5, column=0)

director_input_label = Entry(width=35)
director_input_label.grid(row=5, column=1)

language_input_label = Label(text="Language:", font=('Arial', 12, 'bold'))
language_input_label.grid(row=6, column=0)

language_input_label = Entry(width=35)
language_input_label.grid(row=6, column=1)

IMDB = Label(text="IMDB Rating:", font=('Arial', 12, 'bold'))
IMDB.grid(row=7, column=0)

imdb_input = Entry(width=35)
imdb_input.grid(row=7, column=1)

get_details = Button(text='Get details', highlightthickness=0, command=movie_details)
get_details.grid(column=1, row=8)

clear_details = Button(text='clear', highlightthickness=0, command=clear_button)
clear_details.grid(column=1, row=9)

window.mainloop()
