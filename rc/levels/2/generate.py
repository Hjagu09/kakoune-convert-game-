from random import randint

data = ""
keys = list("abcdefghijklmnopqrstuvwxyz")
first = 0
for i in range(len(keys) * len(keys)):
	line = []
	if i % len(keys) == 0 and i != 0:
		first += 1
	name = keys[first] + keys[i % len(keys)]
	for j in range(randint(1, 20)):
		line.append(str(randint(0, 1000)))
	data += f"\n{name * randint(1, 3)}, {', '.join(line)}"

with open("input", "w") as file:
	file.write(data.strip("\n"))
