from sys import argv
from os.path import realpath, dirname


with open(dirname(realpath(__file__)) + "/solution") as correct:
	if correct.read().strip("\n").strip(" ") != argv[1].strip("\n").strip(" "):
		print("incorrect")
		exit(-1)

print("correct")
