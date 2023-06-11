# Random Movie Picker

This is a Python application that helps you randomly select a movie to watch from the top-rated movies on IMDb. It uses web scraping to retrieve movie information from the IMDb website and presents it to you in a user-friendly graphical interface.

## Installation

To run this application, make sure you have the following dependencies installed:

- `beautifulsoup4`
- `requests`
- `tkinter`
- `Pillow`

You can install these dependencies by running the following command:

```shell
pip install beautifulsoup4 requests Pillow
```

## Usage

To use the application, follow these steps:

1. Run the Python script `random_movie_picker.py` in your Python environment.
2. The application will fetch the top-rated movies from the IMDb website.
3. A graphical interface will open, displaying the title and release year of a randomly selected movie.
4. Click on the provided link to open the IMDb page of the selected movie.
5. A popup will appear, asking if you have already watched the movie.
6. Choose your response by clicking either "Yes" or "No" in the popup.
   - If you click "No", a message will be displayed, indicating that you can click the link to visit the movie's website.
   - If you click "Yes", a new movie will be randomly selected, and the process repeats.

## GUI

The application provides a graphical user interface (GUI) for ease of use. The GUI features a background image and the following components:

- Movie title label: Displays the title and release year of the selected movie.
- Movie URL label: Displays the IMDb URL of the selected movie. Clicking on the link opens the movie's IMDb page.
- Generate button: Triggers the selection of a new random movie.
- Quit button: Closes the application.

## Note

The code includes commented sections that allow the application to be used in a terminal instead of the GUI. If you prefer to run the application in a terminal, you can uncomment those sections and comment out the GUI-related code.

Enjoy your movie!
