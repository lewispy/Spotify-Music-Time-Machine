import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from billboard import Billboard


class PlaylistManager:
	def __init__(self, playlist_name, playlist_description, billboard: Billboard):
		# initialise global vars
		self.playlist_name = playlist_name
		self.playlist_description = playlist_description
		self.billboard = billboard
		self.c_id = os.getenv("SPOTIFY_CLIENT_ID")
		self.c_sec = os.getenv("SPOTIFY_CLIENT_SECRET")
		self.r_uri = os.getenv("SPOTIFY_REDIRECT_URI")
		self.username = "lewis"
		self.scope = "playlist-modify-public"
		self.message = ""

		# Instantiate the spotipy object
		self.sp = spotipy.Spotify(
			auth_manager=SpotifyOAuth(
				client_id=self.c_id,
				client_secret=self.c_sec,
				scope=self.scope,
				redirect_uri=self.r_uri,
				cache_path="token.txt",
				username=self.username,
			)
		)

	# Extract user id of current user
	def __extract_id(self):
		user_id = self.sp.current_user()["id"]
		return user_id

	# Create a playlist for current user
	def __create_playlist(self):
		user_id = self.__extract_id()

		# First load existing playlists to check if current creation already exists
		pre_playlist = self.sp.user_playlists(user=user_id)
		playlist_names = [pre_playlist["items"][i]["name"] for i, _ in enumerate(pre_playlist["items"])]

		if self.playlist_name in playlist_names:
			self.message = f"Playlist \"{self.playlist_name}\" already exists in user's library."
			return None

		self.sp.user_playlist_create(
			user=user_id,
			name=self.playlist_name,
			description=self.playlist_description,
			public=True,
		)
		post_playlist = self.sp.user_playlists(user=user_id)  # Load the user's playlists again to extract its uri
		playlist_id = post_playlist["items"][0]["id"]  # The newly created playlist should be in index 0

		return playlist_id  # return the new playlist's uri

	# Populate the new playlist with tracks from user provided date
	def populate_playlist(self):
		playlist_id = self.__create_playlist()
		print(playlist_id)

		if playlist_id is None:
			return
		else:
			track_list = self.billboard.get_tracks()
			track_uris = []
			for track in track_list:
				track_year = f"track:{track} year:{self.billboard.year}"
				track_feedback = self.sp.search(q=track_year, type="track")
				try:
					track_uri = track_feedback["tracks"]["items"][0]["uri"]
					track_uris.append(track_uri)
				except IndexError:
					pass

			self.sp.playlist_add_items(
				playlist_id=playlist_id,
				items=track_uris,
			)
		self.message = "Successfully added tracks to playlist"
