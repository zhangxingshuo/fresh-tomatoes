import webbrowser

class Movie():
    '''
    Class for defining a movie to display on a webpage
    Movie title, a URL to a poster, and a YouTube link
    to the trailer are the parameters.
    '''
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)