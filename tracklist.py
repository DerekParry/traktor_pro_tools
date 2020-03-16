#!ve/bin/python3

import xml.etree.ElementTree as ET
import argparse
import configparser
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--playlistname', required=False)
    parser.add_argument('--archivename', required=False)
    args = parser.parse_args()
    return args.playlistname, args.archivename

def get_xml_root(path):
	tree = ET.parse(path)
	return tree.getroot()

def get_file_paths():
	config = configparser.ConfigParser()
	config.read('config.ini')
	collection_file_path = config['paths']['COLLECTION_FILE']
	history_dir_path = config['paths']['HISTORY_DIR']
	return collection_file_path, history_dir_path

def get_track_name(root, pk):
		key = pk.get('KEY')
		file_start_index = key.rfind('/:') + 2
		file_dir = key[:file_start_index]
		file_name = key[file_start_index:]

		entry = root.find(f'COLLECTION/ENTRY/LOCATION[@FILE="{file_name}"]...')
		artist = entry.get('ARTIST')
		title = entry.get('TITLE')
		return f'{artist} - {title}' if artist else title

def print_tracklist(tracklist):
	for index, track in enumerate(tracklist):
		print(f'{index+1:02}.\t{track}')

def get_history(path):
	root = get_xml_root(path)
	tracklist = []

	for pk in root.findall('PLAYLISTS/NODE/SUBNODES/NODE/PLAYLIST/ENTRY/PRIMARYKEY'):
		track = get_track_name(root, pk)
		tracklist.append(track)

	print_tracklist(tracklist)

def get_playlist(collection_file_path, name):
	root = get_xml_root(collection_file_path)
	playlist = root.find(f'PLAYLISTS/NODE/SUBNODES/NODE[@NAME="{name}"]')

	print('------------------------')
	print(f'PLAYLIST: {name}')
	print('------------------------')
	
	tracklist = []
	for pk in playlist.findall('PLAYLIST/ENTRY/PRIMARYKEY'):
		track = get_track_name(root, pk)
		tracklist.append(track)

	print_tracklist(tracklist)

def main():
	playlistname, archivename = parse_args()
	collection_file_path, history_dir_path = get_file_paths()

	if playlistname:
		get_playlist(collection_file_path, playlistname)
	if archivename:
		get_history(history_dir_path + archivename + '.nml')


if __name__ == '__main__':
	main()
