import click

## import useful functions
from .helpers import (
	get_movies_from_api,
)


__author__ = 'Dominik Pioś'


@click.group()
def main():
	"""
	Command Line Interface for querying movies
	"""
	pass


@main.command()
def add():
	"""
	Search for movies by typing movie names
	"""
	try:
		open('key.txt')

		arr_of_movies = []
		arr_of_movies.append(click.prompt(
			'Type movie name',
			type=str
		))

		while click.confirm('Do you want to add more movies?'):
			arr_of_movies.append(click.prompt(
				'Type movie name',
				type=str
			))

		movies = get_movies_from_api(arr_of_movies)

		if len(movies) != 0:
			click.echo("We've found these movies:")

			x = 1

			for movie in movies:
				click.echo(f"{x}. {movie['Title']}")
				x += 1
		
		else:
			click.echo("Sorry :( We haven't found any movie")
	except OSError:
		click.echo("You must provide your API Key first! Type 'movies key'")


@main.command()
@click.option(
	'--p',
	prompt='Provide your api key',
)
def key(p):
	"""
	User can provide his api key
	"""
	with open('key.txt', 'w') as file:
		file.write(p)

	click.echo('API Key added')