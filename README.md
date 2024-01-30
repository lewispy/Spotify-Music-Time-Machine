<p align="center"><img src="https://github.com/lewispy/Spotify-Music-Time-Machine/blob/main/images/app_image.png"></p>

##
# Spotify Music Time Machine
Welcome to the Spotify Music Time Machine, a Python application that lets you travel back in time and create nostalgic Spotify playlists based on Billboard Hot 100 charts from specific dates.

## Features
+ Date Selection: Enter a specific date in the format "YYYY-MM-DD" to explore the Billboard Hot 100 chart for that day.
+ Playlist Creation: Create a new Spotify playlist with tracks from the selected date's Billboard Hot 100 chart.
+ Automatic Exclusion: Automatically skips tracks that are not available on Spotify, ensuring a seamless playlist creation process.
+ User-Friendly Interface: The graphical user interface (GUI) provides an intuitive and easy-to-use experience.

## How to Use
+ Enter the target date in the "Enter a date" field.
+ Provide a name for your playlist in the "Enter playlist name" field.
+ Optionally, add a description for your playlist in the "Enter playlist description" text area.
+ Click the "Create" button to generate a new playlist on your Spotify account.

## Requirements
+ Python 3.x
+ Spotipy: A Python library for the Spotify Web API.
+ Beautiful Soup: A library for pulling data out of HTML and XML files.
+ Requests: A Python library for making HTTP requests.

## Assumptions
+ User is has a Spotify account
+ User has created a developer account on Spotify
+ User has stored their client id and client secret as environment variables SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET respectively

## Installation
+ Clone the repository: git clone https://github.com/your-username/spotify-music-time-machine.git
+ Install dependencies: pip install -r requirements.txt
+ Set up Spotify API credentials by creating a Spotify Developer account and updating the .env file.

## Acknowledgements
This app uses the Spotify Web API and Billboard charts data to create nostalgic playlists.
##
Feel free to explore, contribute, and share your musical journey with the Spotify Music Time Machine!
