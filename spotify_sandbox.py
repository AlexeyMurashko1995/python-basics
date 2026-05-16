import pandas as pd
import sqlite3

music_data = {
    'track_name': ['Blinding Lights', 'Starboy', 'Shape of You', 'Believer', 'Flowers'],
    'artist': ['The Weeknd', 'The Weeknd', 'Ed Sheeran', 'Imagine Dragons', 'Miley Cyrus'],
    'genre': ['Pop', 'R&B', 'Pop', 'Rock', 'Pop'],
    'plays_millions': [3700, 2900, 3500, 2700, 1600],
    'release_year': [2019, 2016, 2017, 2017, 2023]
}

df = pd.DataFrame(music_data)

conn = sqlite3.connect('spotify_tracks.db')

