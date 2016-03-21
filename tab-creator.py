#!/usr/bin/env
import os.path

def setup():
	name = raw_input("Please enter your name: ")
	song = raw_input("Please enter the song name: ")
	song = song.replace(" ", "_")
	song_name = song
	song += '.txt'	
	artist = raw_input("Please enter the artist: ")
	tuning = raw_input("Please enter the song tuning (standard, drop-d, drop-c, d-standard): ")
	path_name = 'tabs/'
	path_to_file = os.path.join(path_name, song)

	f = open(path_to_file, 'w')
	f.write("Author: %s\n" % name)
	f.write("Song: %s\n" % song_name)
	f.write("Artist: %s\n" % artist)

if __name__ == "__main__":
	setup()
