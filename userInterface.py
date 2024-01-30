from tkinter import *
import re
from billboard import Billboard
from playlistManager import PlaylistManager

with open("colors.txt") as f:
	lines = f.readlines()

BG_COLOR = lines[0].strip()
BUTTON_TEXT_COLOR = lines[1].strip()
BUTTON_COLOR = lines[2].strip()
ENTRY_BG_COLOR = lines[3].strip()
ENTRY_FONT = "Courier"


class UserInterface:
	def __init__(self):
		self.window = Tk()
		self.window.title("Welcome to the Spotify Music Time Machine")
		self.window.resizable(width=False, height=False)
		self.window.config(bg=BG_COLOR, padx=20, pady=20, width=620, height=540)

		self.canvas_img = PhotoImage(file="./images/spotify_logo.png")
		self.manager = None
		self.board = None

		self.canvas = Canvas(
			width=592,
			height=179,
			bg=BG_COLOR,
			highlightthickness=0,
		)
		self.canvas.create_image(
			296, 89.5,
			image=self.canvas_img
		)
		self.canvas.grid(row=0, column=0, columnspan=2)

		self.date_entry_label = Label(
			font=(ENTRY_FONT, 13, "italic"),
			text="Enter a date",
			bg=BG_COLOR,
			fg="white"
		)
		self.date_entry_label.grid(row=1, column=0, sticky="E")

		self.date_entry = Entry(
			font=(ENTRY_FONT, 13),
			width=20,
			bg=ENTRY_BG_COLOR
		)
		self.date_entry.insert(0, "YYYY-MM-DD")
		self.date_entry.grid(row=1, column=1)

		self.name_entry_label = Label(
			font=(ENTRY_FONT, 13, "italic"),
			text="Enter playlist name",
			bg=BG_COLOR,
			fg="white"
		)
		self.name_entry_label.grid(row=2, column=0, sticky="E")

		self.name_entry = Entry(
			font=(ENTRY_FONT, 13),
			width=20,
			bg=ENTRY_BG_COLOR
		)
		self.name_entry.grid(row=2, column=1)

		self.description_entry_label = Label(
			font=(ENTRY_FONT, 13, "italic"),
			text="Enter playlist description",
			bg=BG_COLOR,
			fg="white"
		)
		self.description_entry_label.grid(row=3, column=0, sticky="E")

		self.description_entry = Text(
			font=(ENTRY_FONT, 13),
			width=20,
			height=3,
			bg=ENTRY_BG_COLOR
		)
		self.description_entry.grid(row=3, column=1)

		self.f1 = Frame(
			self.window,
			bg=BG_COLOR,
			highlightthickness=0,
		)
		self.f1.grid(row=4, column=0, columnspan=2, pady=15)

		self.cancel_button = Button(
			self.f1,
			bg=BUTTON_COLOR,
			fg=BUTTON_TEXT_COLOR,
			height=2,
			width=12,
			text="Cancel",
			font=(ENTRY_FONT, 12, "bold"),
			command=self.close_window,
		)
		self.cancel_button.grid(row=0, column=0, sticky="W")

		self.create_button = Button(
			self.f1,
			bg=BUTTON_COLOR,
			fg=BUTTON_TEXT_COLOR,
			height=2,
			width=12,
			text="Create",
			font=(ENTRY_FONT, 12, "bold"),
			command=self.check_entries,
		)
		self.create_button.grid(row=0, column=1, sticky="E")

		self.message_label = Label(
			font=(ENTRY_FONT, 12),
			text=" ",
			bg=BG_COLOR,
			fg="white",
		)
		self.message_label.grid(row=5, column=0, columnspan=2)

		self.window.mainloop()

	def close_window(self):
		self.window.destroy()

	def warning_box(self):
		warning = Toplevel(
			self.window,
			width=200,
			height=400,
			pady=20,
			padx=20,
			bg=BG_COLOR,
		)

		warning_message = Label(
			warning,
			font=(ENTRY_FONT, 20, "bold"),
			bg=BG_COLOR,
			fg="red",
			text="Invalid date!!!\nDate should be in format YYYY-MM-DD"
		)
		warning_message.grid(row=0, column=0)

	def check_entries(self):
		date = self.date_entry.get().strip()
		playlist_name = self.name_entry.get().strip()
		description = self.description_entry.get("1.0", "end-1c").strip()
		pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

		if len(playlist_name) == 0:
			playlist_name = f"My Oldies from {date}"

		if not pattern.match(date):
			self.warning_box()
		else:
			self.board = Billboard(date)
			self.manager = PlaylistManager(playlist_name, description, self.board)
			self.manager.populate_playlist()
			self.message_label.config(
				text=self.manager.message
			)
