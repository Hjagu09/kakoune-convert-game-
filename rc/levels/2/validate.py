import json
import csv
from sys import argv
from os.path import realpath, dirname

csv_data = {}
json_data = None

# JSON loading
try:
	json_data = json.loads(argv[1])
except json.decoder.JSONDecodeError:
	print("incorrect (bad json)")
	exit(2)

# CSV loading
with open(dirname(realpath(__file__)) + "/input") as csv_file:
	reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
	raw_data = list(reader)
	for i in range(len(raw_data)):
		csv_data[raw_data[i][0]] = [int(x) for x in raw_data[i][1:]]

if csv_data != json_data:
	print("incorrect")
	exit(1)
print("correct")
