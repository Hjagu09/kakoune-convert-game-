#!/usr/bin/env python3
import argparse
import json
from os.path import realpath, dirname
from pathlib import Path
from cli_frontend import cli
import subprocess


def default(args):
	try:
		# paths and intit
		frontend = cli()
		cwd = Path(dirname(realpath(__file__)))
		rc = cwd / "../../rc/"
		level = rc / "levels" / str(args.level)

		# level description
		frontend.info(open(level / "info.md").read(), True)

		# start kakoune and time the user
		cmd = [
			str(cwd / "start_chalange.bash"),  # script to run challenge
			str(cwd),
			str(level / "input")  # challenge input
		]
		frontend.count_down(rc / "numbers")
		process = subprocess.Popen(
			" ".join(cmd),
			stderr=subprocess.PIPE,
			shell=True
		)
		output, error = process.communicate()
		try:
			time_parts = [
				float(x) for x in
				error.decode("utf-8").split("\n")[-2].split(":")
			]
		except Exception as e:
			print(error.decode("utf-8"))
			print(" ".join(cmd))
			raise e
		time = 60 * time_parts[0] + time_parts[1]

		# validate the solution
		with open(cwd / "../../rc/working/input") as file:
			solution = file.read()
			cmd = [
				"python3",
				str(level / "validate.py"),  # validation script
				solution
			]
			return_code = subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode
			# return_code = subprocess.run(cmd).returncode
			if return_code != 0:
				print("that's not the correct solution")
				exit()

		# correct (display time)
		frontend.info(f"\nYou completed the challenge in {time} seconds 🥳🥳🥳", False)
		
	except KeyboardInterrupt:
		exit()
	except EOFError:
		exit()


def list_levels(args):
	frontend = cli()
	cwd = Path(dirname(realpath(__file__)))
	rc = cwd / "../../rc/"
	level_dir = rc / "levels"
	with open(level_dir / "level_data.json") as json_file:
		level_data = json.load(json_file)
		frontend.print_levels(level_data)


# argparse, paths and frontend init
parser = argparse.ArgumentParser(
	"kak_converts"
)
subcommands = parser.add_subparsers()
default_parser = subcommands.add_parser("play", help="play a level")
default_parser.add_argument(
	help="select an level",
	type=int,
	dest="level"
)
default_parser.set_defaults(func=default)
list_parser = subcommands.add_parser("list", help="list all levels")
list_parser.set_defaults(func=list_levels)

args = parser.parse_args()
args.func(args)
