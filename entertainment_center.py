import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https:/upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()
hunger_games = media.Movie("Hunger Games",
                     "A really real reality show",
                     "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://youtube/watch?v=PbA63a7H0bo")
ratatouille = media.Movie("Ratatouille",
                     "A rat is a chef in Paris",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://youtube.com/watch?v=c3sBBRxDAqk")
matrix = media.Movie("Matrix",
                     "Awesome freakin flick",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://youtu.be/m8e-FF8MsqU")
movies = [toy_story, avatar, matrix, ratatouille, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
print(media.Movie.__doc__)
