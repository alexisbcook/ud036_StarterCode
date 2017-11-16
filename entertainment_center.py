import fresh_tomatoes
import media

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"http://www.youtube.com/watch?v=-9ceBgWV8io")

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=4KPTXpQehio")

ratatouille = media.Movie("Ratatouille",
	"A rat becomes a chef",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://youtube.com/watch=?v=c3sBBRxDAqk")

# create list of movies
movies = [avatar, toy_story, ratatouille]
# generate html file with movie trailer
fresh_tomatoes.open_movies_page(movies)