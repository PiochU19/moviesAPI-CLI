import click

## import useful functions
from .helpers import (
	get_movies_from_api,
	add_movies_to_csv_file,
	sort_movies_by_imdb,
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
		f = open('key.txt')
		f.close()

		movies = []
		movies.append(click.prompt(
			'Type movie name',
			type=str
		))

		while click.confirm('Do you want to add more movies?'):
			movies.append(click.prompt(
				'Type movie name',
				type=str
			))

		movies = get_movies_from_api(movies) ## calling API

		if len(movies) != 0:
			click.echo("We've found these movies:")

			x = 1

			for movie in movies:
				click.echo(f"{x}. {movie['Title']} directed by {movie['Director']}")
				x += 1

			if click.confirm('Do you want to add these movies to your library?'):
				add_movies_to_csv_file(movies)

				click.echo('Movies added')
		
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
	You can provide your api key
	"""
	with open('key.txt', 'w') as file:
		file.write(p)

	click.echo('API Key added')


@main.command()
@click.option(
	'--l',
	default=1,
)
def top(l):
	"""
	Shows top movies
	"""
	movies = sort_movies_by_imdb()

	if movies:
		if l > len(movies):
			l = len(movies)

		click.echo(f"Here are your top {l} movies")

		for i in range(l):
			click.echo(f"{i+1}. {movies[i][0]} IMDB rating: {movies[i][1]}")
	else:
		click.echo("You don't have any movies")


@main.command()
def all():
	"""
	Shows all titles
	"""
	titles = 
