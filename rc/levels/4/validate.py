from sys import argv
from os.path import realpath, dirname
import json


with open(dirname(realpath(__file__)) + "/solution") as correct:
	try:
		if json.load(correct) != json.loads(argv[1]):
			print("incorrect")
			exit(-1)
	except json.JSONDecodeError:
		print("incorrect (bad json)")
		exit(-1)

print("correct")
