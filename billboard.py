from bs4 import BeautifulSoup
import requests


class Billboard:
	def __init__(self, date):
		self.date = date
		if self.date is not None:
			self.year = date.split("-")[0]
			self.link = "https://www.billboard.com/charts/hot-100/"+self.date

	def get_tracks(self):
		response = requests.get(url=self.link)
		website_html = response.text

		soup = BeautifulSoup(website_html, "html.parser")
		titles = [title.getText().strip() for title in soup.select("li ul li h3")]

		return titles
