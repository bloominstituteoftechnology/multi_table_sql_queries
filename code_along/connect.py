import sqlite3
import queries as q

conn = sqlite3.connect('chinook.db')

curs = conn.cursor()

if __name__ == '__main__':
    print('How many Genres?')
    print(curs.execute(q.NUM_GENRES).fetchall())

    print('\nHow many Albums?')
    print(curs.execute(q.NUM_ALBUMS).fetchall())

    print('\nHow many Artists?')
    print(curs.execute(q.NUM_ARTISTS).fetchall())

    print('\nHow many Tracks?')
    print(curs.execute(q.NUM_TRACKS).fetchall())

    print('\nWhat is the Genre with the greatest number of albums?')
    print(curs.execute(q.MOST_ALBUMS_GENRE).fetchall())

    print('\nWhat is then name of the artist that has written the most albums?')
    print(curs.execute(q.MOST_ALBUMS_ARTIST).fetchall())

    print('\nWhat is the name of the playlist with the longest runtime?')
    print(curs.execute(q.LONGEST_PLAYLIST).fetchall())

    print('\nWhat is the name of the artist that writes the shortest songs –on average?')
    print(curs.execute(q.SHORT_SONG_ARTIST).fetchall())

    print('\nWhich employee has been the Support Rep for the greatest number of customers?')
    print(curs.execute(q.BUSIEST_SUPPORT_REP).fetchall())
