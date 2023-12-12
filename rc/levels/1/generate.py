from random import randint

data = ""

for i in range(500):
	line = []
	for j in range(randint(10, 50)):
		line.append(str(randint(0, 100000)))
	data += f"\n{', '.join(line)}"

with open("input", "w") as file:
	file.write(data.strip("\n"))
