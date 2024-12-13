import tkinter as tk
from PIL import Image, ImageTk
from stats_logic import fetch_player_stats


def display_error(message):
    """
    Display error messages in the output text area.
    """
    output_text.delete("1.0", tk.END)  # Clear any previous output
    output_text.insert(tk.END, f"Error: {message}\n")


def fetch_and_display_stats():
    """
    Fetch player stats and display them in the output text area.
    """
    player_name = player_name_entry.get().strip()
    if not player_name:
        display_error("Please enter a player's name.")
        return

    # Fetch player stats
    stats = fetch_player_stats(player_name)

    if "error" in stats:
        display_error(stats["error"])
        return

    # Clear existing text
    output_text.delete("1.0", tk.END)

    # Display stats
    output_text.insert(tk.END, f"Team: {stats['team']}\n")
    output_text.insert(tk.END, f"Position: {stats['position']}\n")
    output_text.insert(tk.END, f"Games Played: {stats['games_played']}\n")
    output_text.insert(tk.END, f"Points Per Game (PPG): {stats['ppg']:.1f}\n")
    output_text.insert(tk.END, f"Rebounds Per Game (RPG): {stats['rpg']:.1f}\n")
    output_text.insert(tk.END, f"Assists Per Game (APG): {stats['apg']:.1f}\n")
    output_text.insert(tk.END, f"Blocks Per Game (BPG): {stats['bpg']:.1f}\n")
    output_text.insert(tk.END, f"Steals Per Game (SPG): {stats['spg']:.1f}\n")
    output_text.insert(tk.END, f"Field Goal Percentage (FG%): {stats['fg_pct']:.1%}\n")
    output_text.insert(tk.END, f"3-Point Percentage (3P%): {stats['three_pt_pct']:.1%}\n")


def clear_fields():
    """
    Clear the player name input field and the output text area.
    """
    player_name_entry.delete(0, tk.END)  # Clear the input field
    output_text.delete("1.0", tk.END)  # Clear the output area


def create_gui():
    """
    Create the main GUI for the NBA Player Stats Viewer application.
    """
    # Main window setup
    root = tk.Tk()
    root.title("NBA Player Stats Viewer")
    root.geometry("500x600")  # Adjusted size to fit button and other elements
    root.configure(bg="red3")
    root.resizable(False, False)

    # Frame for content
    frame = tk.Frame(root, bg="RoyalBlue3")
    frame.pack(pady=20)

    # Player name input
    player_label = tk.Label(frame, text="Enter Player Name:", font=("Roboto", 12), bg="RoyalBlue3", fg="white")
    player_label.grid(row=0, column=0, padx=10, pady=10)

    global player_name_entry  # Declare as global so fetch_and_display_stats can access it
    player_name_entry = tk.Entry(frame, font=("Roboto", 12), width=30)
    player_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Fetch stats button
    fetch_button = tk.Button(frame, text="Get Stats!", command=fetch_and_display_stats, font=("Roboto", 12, 'bold'), bg="lightgray", fg="red3")
    fetch_button.grid(row=1, column=0, columnspan=2, pady=10, padx=5)

    # Text output
    global output_text  # Declare as global so fetch_and_display_stats can access it
    output_text = tk.Text(root, font=("Roboto", 14), width=40, height=11, wrap="word", bg="white", fg="black")
    output_text.pack(pady=20)

    # Clear button (positioned below output_text and above the logo)
    clear_button = tk.Button(root, text="Clear", command=clear_fields, font=("Roboto", 12, 'bold'), bg="lightgray", fg="red3")
    clear_button.pack(pady=10)  # Add padding to center it nicely

    # Resize NBA logo before adding it
    nba_logo_image = Image.open("/Users/colinroesler/Desktop/nba_logo.png")
    nba_logo_image = nba_logo_image.resize((150, 150))  # Resize it to 150x150 pixels
    nba_logo = ImageTk.PhotoImage(nba_logo_image)  # Convert to Tkinter-compatible format

    # Add NBA logo at the bottom
    logo_label = tk.Label(root, image=nba_logo, bg="red3")
    logo_label.image = nba_logo
    logo_label.pack(side="bottom", pady=20)

    root.mainloop()
