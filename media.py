"""
Code provided in Udacity's Programming Foundations with Python lecture 
"""

import webbrowser


class Movie():
    """stores movie information.

    Attributes:
        title: title of movie
        poster_image_url: url of movie box art
        trailer_youtube_id: youtube video id
        date: release date

    """
    def __init__(self, movie_title, movie_poster_image, movie_date,
                 movie_youtube_id):
        self.title = movie_title
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_id = movie_youtube_id
        self.date = movie_date

    def show_trailer(self):
        """opens default webbrowser to show trailer"""
        
        link = "http://www.youtube.com/embed/" + self.trailer_youtube_id + "?autoplay=1&html5=1"  # NOQA
        webbrowser.open(link)
