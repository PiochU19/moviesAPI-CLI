import requests
import csv


def get_api_key():
	"""
	Function reading api key
	from key.txt
	"""
	with open('key.txt', 'r') as file:
		api_key = file.readline()

	return api_key


def get_movies_from_api(movies):
	"""
	request every movie
	in the given array
	"""
	url_base = 'http://www.omdbapi.com/'
	arr = []
	api_key = get_api_key()

	for movie in movies:
		params = "+".join(movie.split())
		full_url = (
			url_base +
			'?apikey=' +
			api_key +
			'&t=' +
			params
		)
		response = requests.get(full_url)

		if response.status_code == 200 and response.json()['Response'] == 'True':
			arr.append(response.json())

	return arr


def add_movies_to_csv_file(movies):
	"""
	function adding given
	movies to the CSV file
	"""
	try:
		f = open('movies.csv')
		f.close()
		with open('movies.csv', 'a') as file:
			for movie in movies:
				file.write(f"\n{movie['Title']};{movie['imdbRating']};{movie['BoxOffice']}")

	except OSError:
		with open('movies.csv', 'w') as file:
			file.write('Title;imdbRating;BoxOffice')

			for movie in movies:
				file.write(f"\n{movie['Title']};{movie['imdbRating']};{movie['BoxOffice']}")


def sort_movies_by_imdb():
	"""
	function sorting all
	movies by IMDB rating
	"""
	try:
		with open('movies.csv', 'r') as file:
			movies = [x.split(';') for x in list(file)]
			del movies[0]
			sorter = lambda x: (x[1], x[0], x[2])
			movies = sorted(movies, key=sorter, reverse=True)
			return movies
			
	except OSError:
		return False

