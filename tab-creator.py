#!/usr/bin/env
import os.path

def setup():
	# Get user's name
	name = raw_input("Please enter your name: ")
	# Get song name
	song = raw_input("Please enter the song name: ")
	# If user gives whitespace, replace it with an underscore
	song.replace(" ", "_")
	song_name = song
	song += '.txt'
	print "songname: ", song
	# Get the name of the artist
	artist = raw_input("Please enter the artist: ")
	# Set the tuning for the song
	tuning = raw_input("Please enter the song tuning (standard, drop-d): ")
	# Sets path for files to be placed in tabs folder
	path_name = 'tabs/'
	path_to_file = os.path.join(path_name, song)
	# Open the file for writing
	f = open(path_to_file, 'w')
	f.write("Author: %s\n" % name)
	f.write("Song: %s\n" % song_name)
	f.write("Artist: %s\n" % artist)
	f.close()
	# Call the framework function
	framework(path_to_file, tuning)

def framework(path_to_file, tuning):
	tuning_strings = []
	f = open(path_to_file, 'a')
	if (tuning == 'standard'):
		tuning_strings = ['E', 'A', 'D', 'G', 'B', 'E']
	elif (tuning == 'drop-d'):
		tuning_strings = ['D', 'A', 'D', 'G', 'B', 'E']

	for i in range(0, len(tuning_strings)):
		f.write("%s" % tuning_strings[i])
		for i in xrange(1, 5):
			f.write("|--------------------")
		f.write("\n")

if __name__ == "__main__":
	setup()
