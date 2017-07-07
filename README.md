# movie_trailer_website

Final Project for Udacity's Programming Foundations in Python. This is a python program that dynamically generates an html file which displays box art and corresponding trailers.

**Upgrades to the project:**
 - use TMDB API to get movies now playing in theatres
 - use Youtube API to display trailers in lieu of hardcoding urls

## Dependencies
Follow links for additional install options
* [python 2.*](https://www.python.org/download/releases/2.7/)
* [tmdbsimple](https://github.com/celiao/tmdbsimple) wrapper for The Movie Database

  ```
  $ pip install tmdbsimple
  ```

* [YouTube Data API Client Library](https://developers.google.com/api-client-library/python/apis/youtube/v3)

  ```
  $ pip install --upgrade google-api-python-client
  ```


## API Keys
You will need two API keys.  Replace the existing API keys with your keys in the entertainment_center.py file
* _The Movie Database (TMDB):_
    1. [Register for and verify](https://www.themoviedb.org/account/signup) an account
    2. Go to **Settings** by clicking on your avatar
    3. Go to **API** located in the left panel

* _YouTube Data API:_   
    1. [Register and login](https://console.developers.google.com) to Google APIS
    2. Click on **Credentials** in the left panel
    3. Create an API key
    4. Click on **library** in the left panel
    5. Search or scroll down to **YouTube Data API**
    6. Click **Enable** near the top of the screen to use this API

## Run the Program
This will automatically generate a new file "fresh_tomatoes.html" in the directory and automatically open the page in your default browser

```
python entertainment_center.py
```
