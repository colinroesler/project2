"""
This script uses the `nba_api` library from the GitHub repository:
https://github.com/swar/nba_api

This application fetches and displays NBA player statistics based on user input.

The GUI is built using Tkinter, and the stats are fetched from the NBA API.

Main entry point is at the bottom of the file, calling the create_gui function.
"""

from gui import create_gui

if __name__ == "__main__":
    create_gui()  # Call the create_gui function to initialize and run the app
