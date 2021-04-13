# moviesAPI-CLI
📎 Simple Command Line Interface using OMDb API
# Quick introdution to my Project

You can see every command along with what they do
```bash
movies --help
```
You can provide your API KEY
```bash
movies key
```
You can add some movies to your library
```bash
movies add
```
you can see the titles of all movies in your library
```bash
movies all
```
You can see top [x] movies in your library, by default x is 1
```bash
movies top --l x
```
You can see the most profitable movie in your library
```bash
movies profitable
```
You can see average IMDB rating of the movies in your library
```bash
movies avg
```

## Installation

* clone this repo to you local folder 
```bash
git clone https://github.com/PiochU19/moviesAPI-CLI.git
cd moviesAPI-CLI
```
* make your virtualenv
```bash
virtualenv env
```
* and activate it

on Windows:
```bash
env/scripts/activate
```
on macOS and Linux
```bash
source env/scripts/activate
```
* install package 
```bash
pip install .
```
## That's it, everything is set up

Now you can run tests on your local machine by typing:
```bash
py.test
```
As you can see below, I've already done it

![tests](https://github.com/PiochU19/moviesAPI-CLI/blob/main/tests.PNG?raw=true)

### Remember to delete files key.txt and movies.csv after running tests