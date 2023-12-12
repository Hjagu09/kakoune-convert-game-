import json
from random import randint

ini_data = []
json_data = {}

keys = list("abcdefghijklmnopqrstuvwxyz")
first = 0
second = 0


def get_key():
	global second
	global first
	if second % len(keys) == 0 and second != 0:
		first += 1
	name = (keys[first] + keys[second % len(keys)]) * randint(1, 3)
	second += 1
	return name


for i in range(40):
	section_name = get_key()
	ini_data.append(f"\n[{section_name}]")
	section_data = {}
	for j in range(randint(5, 15)):
		key_name = get_key()
		value = randint(-9999, 9999)
		ini_data.append(f"{key_name} = {value}")
		section_data[key_name] = value
		if randint(0, 10) == 5:
			ini_data.append("; bla bla bla")
	json_data[section_name] = section_data

with open("input", "w") as file:
	file.write("\n".join(ini_data))

with open("solution", "w") as file:
	json.dump(json_data, file)
