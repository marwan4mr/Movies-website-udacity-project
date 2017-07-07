#!/usr/bin/python

"""
  Uses tmdbsimple, a wrapper for The Movie Database API v3
  (https://github.com/celiao/tmdbsimple) to generate a list of movies now
  playing in theatres.

  Uses Youtube Data API to view the corresponding trailer
"""
import fresh_tomatoes
import media
import tmdbsimple as tmdb
from apiclient.discovery import build

movie_list = []

# -------TMDB API-------BE SURE TO REPLACE THE KEY FOR YOUR PROJECT-->
tmdb.API_KEY = "c12edf83d870c525a0b7aadd2a7f4ddc"

# ------YOUTUBE API-----BE SURE TO REPLACE THE KEY FOR YOUR PROJECT-->
DEVELOPER_KEY = "AIzaSyDmYfSeVajJKkasfDzU6DHq6_IVhQPemsY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,
                YOUTUBE_API_VERSION,
                developerKey = DEVELOPER_KEY)


current_movies = tmdb.Movies().now_playing()

def youtube_search_id(title):
    search_response = youtube.search().list(q = title,
                                            part = "id",
                                            type = "video",
                                            fields = "items/id/videoId"
                                            ).execute()
    return search_response["items"][0]["id"]["videoId"]


movie_list = []
# instantiate each movie
for movie in current_movies["results"]:
    movie_list.append(media.Movie(movie["title"],
                                  movie["poster_path"],
                                  movie["release_date"],
                                  youtube_search_id(movie["title"])))

fresh_tomatoes.open_movies_page(movie_list)
