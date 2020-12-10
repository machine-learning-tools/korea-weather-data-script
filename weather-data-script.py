import sys
from pathlib import Path

WORKING_DIRECTORY = sys.argv[1]
'''p will be a global variable because we will
use it a lot of times in this script'''
p = Path(WORKING_DIRECTORY)

def get_all_filenames():
	filenames = []
	for file in p.rglob('*.csv'):
		filenames.append(file.name)
	return filenames

def delete_first_line(filename):
	temp_file = open(filename, 'r', errors='ignore')
	lines = temp_file.readlines()
	temp_file.close()
	del lines[0]
	file = open(filename, 'w+')
	for line in lines:
		file.write(line)
	file.close()

def get_unique_station_ids():
	filenames = get_all_filenames()
	filenames = [filename.split('_') for filename in filenames]
	ids = [list[2] for list in filenames]
	unique_ids = list(set(ids))
	unique_ids.sort()
	return unique_ids

def main():
	print(get_all_filenames())
	for file in p.rglob('*.csv'):
		delete_first_line(file.parent / file.name)
	station_ids = get_unique_station_ids()
	for station in station_ids:
		print(station)
		output_file = 'station' + station + '.acsv'
		for file in p.rglob('*.csv'):
			if station in file.name:
				file = open(file.parent / file.name, 'r')
				data = file.readlines()
				file.close()
				output = open(output_file, 'a')
				for line in data:
					output.write(line)
				output.close()

main()
