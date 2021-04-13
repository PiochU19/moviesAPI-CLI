import requests


def get_api_key():
	"""
	Function reading api key
	from key.txt
	"""
	with open('key.txt') as file:
		api_key = file.readline()

	return api_key


def get_movies_from_api(arr_of_movies):
	"""
	request every movie
	in the given array
	"""
	url_base = 'http://www.omdbapi.com/'
	arr = []
	api_key = get_api_key()

	for movie in arr_of_movies:
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