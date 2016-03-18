#!/usr/bin/env

def setup():
	name = raw_input("Please enter your name: ")
	song = raw_input("Please enter the song name: ")
	songName = song
	song += '.txt'
	artist = raw_input("Please enter the artist: ")
	tuning = raw_input("Please enter the song tuning (standard, drop-d, drop-c, d-standard): ")

	f = open(song, 'w')
	f.write("Author: %s\n" % name)
	f.write("Song: %s\n" % songName)
	f.write("Artist: %s\n" % artist)

if __name__ == "__main__":
	setup()
