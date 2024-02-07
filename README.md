# Image Scraping 

Image Scraping using Spotify Developer API

## 1. Filter Relevant Information
[**'get_spotify_id.ipynb'**](https://github.com/KittenSmasher/image-scraping/blob/main/get_spotify_id.ipynb) to select track_id, spotify_id, genre columns from [**'Music Info.csv'**](https://github.com/KittenSmasher/image-scraping/blob/main/Music%20Info.csv). The new data-frame is saved as [**'filtered_info.csv'**](https://github.com/KittenSmasher/image-scraping/blob/main/filtered_info.csv). Track ID that want to be scraped is stored in [**'track_id.txt'**](https://github.com/KittenSmasher/image-scraping/blob/main/track_id.txt).

## 2. Scrap Image
**client_id** and **client_secret** can be found on [Spotify for Developers](developer.spotify.com). The code [**'scrap-image.py'**](https://github.com/KittenSmasher/image-scraping/blob/main/scrap-image.py) is going to read spotify_id and saved its album cover by calling the API. All of the album covers from the filtered_info file will be saved with track_id as its file name and the genre as the folder.
