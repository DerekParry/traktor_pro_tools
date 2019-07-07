import xml.etree.ElementTree as ET


def get_xml_root(path):
	tree = ET.parse(path)
	return tree.getroot()


def get_track_name(root, pk):
		key = pk.get('KEY')
		file_start_index = key.rfind('/:') + 2
		file_dir = key[:file_start_index]
		file_name = key[file_start_index:]

		entry = root.find(f'COLLECTION/ENTRY/LOCATION[@FILE="{file_name}"]...')
		artist = entry.get('ARTIST')
		title = entry.get('TITLE')
		return f'{artist} - {title}'

def print_tracklist(tracklist):
	for index, track in enumerate(tracklist):
		print(f'{index:02}.\t{track}')


def get_history(path):
	root = get_xml_root(path)
	tracklist = []

	for pk in root.findall('PLAYLISTS/NODE/SUBNODES/NODE/PLAYLIST/ENTRY/PRIMARYKEY'):
		track = get_track_name(root, pk)
		tracklist.append(track)

	print_tracklist(tracklist)


def get_playlist(name):
	root = get_xml_root(name)

	# TODO match NAME
	for playlist in root.findall('PLAYLISTS/NODE/SUBNODES/NODE[@TYPE="PLAYLIST"]'):
		print('------------')
		print(playlist.get("NAME"))
		print('------------')
		
		tracklist = []
		for pk in playlist.findall('PLAYLIST/ENTRY/PRIMARYKEY'):
			track = get_track_name(root, pk)
			tracklist.append(track)

		print_tracklist(tracklist)
