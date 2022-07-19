# How many Genres?
NUM_GENRES = '''SELECT COUNT(*) from genres;'''

# How many Albums?
NUM_ALBUMS = '''SELECT COUNT(*) from albums;'''

# How many Artists?
NUM_ARTISTS = '''SELECT COUNT(*) from artists;'''

# How many Tracks?
NUM_TRACKS = '''SELECT COUNT(*) from tracks;'''

# What is the Genre with the greatest number of albums?
MOST_ALBUMS_GENRE = '''
    SELECT genres.Name, COUNT(tracks.AlbumId) as num_albums FROM genres
    JOIN tracks
    ON genres.GenreId = tracks.GenreId
    GROUP BY genres.Name
    ORDER BY num_albums DESC
    LIMIT 1;
'''

# What is then name of the artist that has written the most albums?
MOST_ALBUMS_ARTIST = '''
    SELECT Name, COUNT(AlbumId) as num_albums FROM albums
    JOIN artists
    ON albums.ArtistId = artists.ArtistId
    GROUP BY Name
    ORDER BY num_albums DESC
    LIMIT 1;
'''

# What is the name of the playlist with the longest runtime?
LONGEST_PLAYLIST = '''
    SELECT PlaylistId, SUM(tracks.Milliseconds) AS duration_ms FROM tracks 
    JOIN playlist_track
    ON tracks.TrackId = playlist_track.TrackId
    GROUP BY PlaylistId
    ORDER BY duration_ms DESC
    LIMIT 2;
'''

# What is the name of the artist that writes the shortest songs –on average?

SHORT_SONG_ARTIST = '''
    SELECT artists.Name, AVG(Milliseconds) AS avg_length FROM tracks
    JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    JOIN artists
    ON albums.ArtistId = artists.ArtistId
    GROUP BY artists.Name
    ORDER BY avg_length
    LIMIT 1;
'''

# Which employee has been the Support Rep for the greatest number of customers?
BUSIEST_SUPPORT_REP = '''
    SELECT employees.Firstname, employees.LastName, COUNT(CustomerId)  as num_customers FROM employees
    JOIN customers
    ON customers.SupportRepId = employees.EmployeeId
    GROUP BY EmployeeId
    ORDER BY num_customers DESC
    LIMIT 1;
'''
