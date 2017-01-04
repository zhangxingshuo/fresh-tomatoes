'''
Entertainment Center
====================
Opens a webpage that displays movie posters and trailers.
'''

import media
import fresh_tomatoes

spotlight = media.Movie("Spotlight", 
    "http://www.newdvdreleasedates.com/images/posters/large/spotlight-2015-03.jpg",
    "https://www.youtube.com/watch?v=EwdCIpbTN5g&t=2s")

mad_max = media.Movie("Mad Max: Fury Road",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8")

revenant = media.Movie("The Revenant", 
    "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
    "https://www.youtube.com/watch?v=LoebZZ8K5N0")

big_short = media.Movie("The Big Short",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
    "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

ex_machina = media.Movie("Ex Machina",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=gyKqHOgMi4g")

movie_list = [spotlight, mad_max, revenant, big_short, ex_machina]

fresh_tomatoes.open_movies_page(movie_list)